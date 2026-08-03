# Structured Design Data

This directory contains author-side structured datasets. They are not reader-facing glossaries.

## Current datasets

### 612-system census

The inhabited-system census is split into eight CSV files for maintainability:

- `galaxy-612-system-census-core-v1.csv`
- `galaxy-612-system-census-inner-v1.csv`
- `galaxy-612-system-census-middle-a-v1.csv`
- `galaxy-612-system-census-middle-b-v1.csv`
- `galaxy-612-system-census-middle-c-v1.csv`
- `galaxy-612-system-census-frontier-a-v1.csv`
- `galaxy-612-system-census-frontier-b-v1.csv`
- `galaxy-612-system-census-frontier-c-v1.csv`

Validation:

```bash
python tools/validate_design_data.py
```

The validator checks:

- exactly 612 rows;
- unique system IDs and names;
- exact macroregion counts and registered-population totals;
- exact primary-node quotas;
- 48-cluster distribution;
- allowed GA10 transition seeds;
- required protected systems and locked values.

A dataset is not Working Canon if the validation workflow fails.