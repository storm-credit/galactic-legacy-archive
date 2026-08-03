#!/usr/bin/env python3
"""Generate and validate the canonical author-side 612-system route adjacency.

The exact graph is derived from:
1. the stable census system IDs and cluster memberships;
2. deterministic within-cluster rules;
3. the checked-in 48-cluster backbone.

The generated graph is author-side planning data. It is not a claim that every
route is continuously usable or reader-facing.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

CENSUS_FILES = [
    DATA_DIR / "galaxy-612-system-census-core-v1.csv",
    DATA_DIR / "galaxy-612-system-census-inner-v1.csv",
    DATA_DIR / "galaxy-612-system-census-middle-a-v1.csv",
    DATA_DIR / "galaxy-612-system-census-middle-b-v1.csv",
    DATA_DIR / "galaxy-612-system-census-middle-c-v1.csv",
    DATA_DIR / "galaxy-612-system-census-frontier-a-v1.csv",
    DATA_DIR / "galaxy-612-system-census-frontier-b-v1.csv",
    DATA_DIR / "galaxy-612-system-census-frontier-c-v1.csv",
]

BACKBONE_FILE = DATA_DIR / "galaxy-cluster-backbone-v1.csv"
DEFAULT_OUTPUT = DATA_DIR / "generated" / "galaxy-612-route-adjacency-v1.csv"

NODE_RANK = {"L0": 0, "L1": 1, "L2": 2, "L3": 3}

OUTPUT_COLUMNS = [
    "route_id",
    "system_a_id",
    "system_a_name",
    "system_b_id",
    "system_b_name",
    "cluster_a",
    "cluster_b",
    "route_class",
    "baseline_status",
    "priority_travel_band",
    "civilian_travel_band",
    "source",
    "narrative_note",
]


@dataclass(frozen=True)
class System:
    system_id: str
    name: str
    macro_region: str
    cluster: str
    node: str
    population_m: float
    route_profile: str


@dataclass(frozen=True)
class Edge:
    a: str
    b: str
    route_class: str
    status: str
    priority_band: str
    civilian_band: str
    source: str
    note: str = ""

    def key(self) -> tuple[str, str]:
        return tuple(sorted((self.a, self.b)))  # type: ignore[return-value]


def load_systems() -> tuple[dict[str, System], dict[str, list[System]]]:
    systems: dict[str, System] = {}
    clusters: defaultdict[str, list[System]] = defaultdict(list)
    for path in CENSUS_FILES:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                system = System(
                    system_id=row["system_id"],
                    name=row["system_name"],
                    macro_region=row["macro_region"],
                    cluster=row["cluster"],
                    node=row["primary_node"],
                    population_m=float(row["registered_population_m"]),
                    route_profile=row["route_profile"],
                )
                if system.system_id in systems:
                    raise ValueError(f"duplicate system ID: {system.system_id}")
                systems[system.system_id] = system
                clusters[system.cluster].append(system)
    return systems, dict(clusters)


def gateway(cluster_systems: Iterable[System]) -> System:
    """Select one stable cluster gateway.

    Higher node class wins; population breaks ties; stable ID is final tie-break.
    """

    return sorted(
        cluster_systems,
        key=lambda item: (NODE_RANK[item.node], -item.population_m, item.system_id),
    )[0]


def inferred_local_status(a: System, b: System) -> str:
    profiles = f"{a.route_profile} {b.route_profile}".lower()
    if "damaged" in profiles:
        return "damaged"
    if "seasonal" in profiles or "intermittent" in profiles:
        return "intermittent"
    if "restricted" in profiles:
        return "restricted"
    return "stable"


def local_travel_bands(a: System, b: System, spoke: bool) -> tuple[str, str]:
    if a.node in {"L0", "L1"} or b.node in {"L0", "L1"}:
        return ("0.5–1.5 days", "1–4 days")
    if spoke:
        return ("0.5–2 days", "1–6 days")
    return ("0.5–2.5 days", "1–8 days")


def add_edge(edges: dict[tuple[str, str], Edge], edge: Edge) -> None:
    if edge.a == edge.b:
        raise ValueError(f"self edge: {edge.a}")
    key = edge.key()
    existing = edges.get(key)
    if existing is None:
        edges[key] = edge
        return
    # Backbone/explicit edges override generated local duplicates.
    if existing.source != "cluster backbone" and edge.source == "cluster backbone":
        edges[key] = edge


def build_local_edges(
    systems: dict[str, System],
    clusters: dict[str, list[System]],
    edges: dict[tuple[str, str], Edge],
) -> dict[str, System]:
    gateways: dict[str, System] = {}

    for cluster_name, members_unsorted in sorted(clusters.items()):
        members = sorted(members_unsorted, key=lambda item: item.system_id)
        if len(members) < 2:
            raise ValueError(f"cluster has fewer than two systems: {cluster_name}")

        hub = gateway(members)
        gateways[cluster_name] = hub

        # Local ring guarantees at least two local connections per system.
        for index, a in enumerate(members):
            b = members[(index + 1) % len(members)]
            priority, civilian = local_travel_bands(a, b, spoke=False)
            add_edge(
                edges,
                Edge(
                    a=a.system_id,
                    b=b.system_id,
                    route_class="cluster local ring",
                    status=inferred_local_status(a, b),
                    priority_band=priority,
                    civilian_band=civilian,
                    source="deterministic local ring",
                    note=f"{cluster_name} local continuity route",
                ),
            )

        # Gateway spokes connect all L0/L1/L2 systems and every third L3 system.
        for index, member in enumerate(members):
            if member.system_id == hub.system_id:
                continue
            should_connect = member.node in {"L0", "L1", "L2"} or index % 3 == 0
            if not should_connect:
                continue
            priority, civilian = local_travel_bands(hub, member, spoke=True)
            add_edge(
                edges,
                Edge(
                    a=hub.system_id,
                    b=member.system_id,
                    route_class="cluster gateway spoke",
                    status=inferred_local_status(hub, member),
                    priority_band=priority,
                    civilian_band=civilian,
                    source="deterministic gateway spoke",
                    note=f"{cluster_name} gateway access",
                ),
            )

    return gateways


def backbone_travel(route_class: str, status: str) -> tuple[str, str]:
    route_class_lower = route_class.lower()
    if "anchor" in route_class_lower or "trunk" in route_class_lower:
        priority = "0.5–2 days"
        civilian = "1–6 days"
    elif "frontier bridge" in route_class_lower:
        priority = "1–5 days"
        civilian = "3–18 days"
    elif "cross frontier" in route_class_lower:
        priority = "2–8 days"
        civilian = "5–30 days"
    else:
        priority = "1–4 days"
        civilian = "2–14 days"

    if status in {"damaged", "intermittent"}:
        priority += " when open"
        civilian += " or longer"
    elif status == "restricted":
        civilian += " plus authorization delay"
    return priority, civilian


def add_backbone_edges(
    systems: dict[str, System],
    gateways: dict[str, System],
    edges: dict[tuple[str, str], Edge],
) -> None:
    with BACKBONE_FILE.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            cluster_a = row["cluster_a"]
            cluster_b = row["cluster_b"]
            if cluster_a not in gateways or cluster_b not in gateways:
                raise ValueError(
                    f"backbone references unknown cluster: {cluster_a!r}, {cluster_b!r}"
                )
            a = gateways[cluster_a]
            b = gateways[cluster_b]
            priority, civilian = backbone_travel(
                row["route_class"], row["default_status"]
            )
            add_edge(
                edges,
                Edge(
                    a=a.system_id,
                    b=b.system_id,
                    route_class=row["route_class"],
                    status=row["default_status"],
                    priority_band=priority,
                    civilian_band=civilian,
                    source="cluster backbone",
                    note=row["narrative_note"],
                ),
            )


def build_graph() -> tuple[dict[str, System], list[Edge]]:
    systems, clusters = load_systems()
    edges_by_key: dict[tuple[str, str], Edge] = {}
    gateways = build_local_edges(systems, clusters, edges_by_key)
    add_backbone_edges(systems, gateways, edges_by_key)
    return systems, sorted(edges_by_key.values(), key=lambda edge: edge.key())


def validate_graph(systems: dict[str, System], edges: list[Edge]) -> None:
    adjacency: defaultdict[str, set[str]] = defaultdict(set)
    for edge in edges:
        if edge.a not in systems or edge.b not in systems:
            raise ValueError(f"edge references missing system: {edge}")
        adjacency[edge.a].add(edge.b)
        adjacency[edge.b].add(edge.a)

    missing = sorted(system_id for system_id in systems if not adjacency[system_id])
    if missing:
        raise ValueError(f"systems with no routes: {missing[:10]}")

    low_degree = sorted(
        (system_id, len(neighbors))
        for system_id, neighbors in adjacency.items()
        if len(neighbors) < 2
    )
    if low_degree:
        raise ValueError(f"systems with degree < 2: {low_degree[:10]}")

    start = next(iter(systems))
    visited = {start}
    queue: deque[str] = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in adjacency[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    if len(visited) != len(systems):
        missing_count = len(systems) - len(visited)
        raise ValueError(f"route graph is disconnected; unreachable systems: {missing_count}")

    if not (900 <= len(edges) <= 1800):
        raise ValueError(f"unexpected route count {len(edges)}; expected 900–1800")


def write_graph(systems: dict[str, System], edges: list[Edge], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        for index, edge in enumerate(edges, start=1):
            a = systems[edge.a]
            b = systems[edge.b]
            writer.writerow(
                {
                    "route_id": f"RT-{index:04d}",
                    "system_a_id": a.system_id,
                    "system_a_name": a.name,
                    "system_b_id": b.system_id,
                    "system_b_name": b.name,
                    "cluster_a": a.cluster,
                    "cluster_b": b.cluster,
                    "route_class": edge.route_class,
                    "baseline_status": edge.status,
                    "priority_travel_band": edge.priority_band,
                    "civilian_travel_band": edge.civilian_band,
                    "source": edge.source,
                    "narrative_note": edge.note,
                }
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate the graph and print statistics without writing output",
    )
    args = parser.parse_args()

    try:
        systems, edges = build_graph()
        validate_graph(systems, edges)
    except (OSError, ValueError, KeyError) as exc:
        print(f"ROUTE GRAPH VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    if not args.check:
        output = args.output
        if not output.is_absolute():
            output = ROOT / output
        write_graph(systems, edges, output)
        print(f"wrote {len(edges)} routes to {output.relative_to(ROOT)}")

    print("ROUTE GRAPH VALIDATION PASSED")
    print(f"- systems: {len(systems)}")
    print(f"- undirected routes: {len(edges)}")
    print("- connected: yes")
    print("- minimum degree: >= 2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
