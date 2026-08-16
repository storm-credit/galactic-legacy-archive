from pathlib import Path
ROOT=Path('manuscript/ga1')

def rep(fn,old,new):
    p=ROOT/fn
    t=p.read_text(encoding='utf-8')
    n=t.count(old)
    if n!=1: raise SystemExit(f'{fn}: expected block once, got {n}: {old[:100]!r}')
    p.write_text(t.replace(old,new,1),encoding='utf-8')

rep('043-돌려받지-않는-코어-v1.md', '''다음 화면에 일곱 항목이 올라왔다.\n\n[AUTHORITY CLASS A — PARTIAL RESPONSE]\n\n[AUTHORITY CLASS B — PARTIAL / PROTECTED CONTINUITY PATTERN]\n\n[C — UNKNOWN]\n\n[D — UNKNOWN]\n\n[E — UNKNOWN]\n\n[F — UNKNOWN]\n\n[G — UNKNOWN]''', '''다음 화면에 일곱 분류가 한 번에 올라왔다.\n\n[AUTHORITY: A PARTIAL / B PARTIAL—PROTECTED CONTINUITY / C–G UNKNOWN]''')

rep('044-다시-조립된-07호-v1.md', '''[TEST PURPOSE CONFIRMED]\n\n[PHYSICAL CUSTODY — OPEN]\n\n[LEGACY/CORE AUTHORITY — OPEN]\n\n[CERTIFIED POWER ENVELOPE — OPEN]\n\n[AUDIT/DATA SCOPE — OPEN]''', '''[TEST PURPOSE CONFIRMED — PHYSICAL CUSTODY / LEGACY-CORE AUTHORITY / CERTIFIED POWER ENVELOPE / AUDIT-DATA SCOPE: OPEN]''')

rep('065-죽은-사람에게-필요한-약-v1.md', '''[동의된 과정증명: 공개신원 폐쇄와 임상연속의 병존]\n\n[선택 환자 현재 임상존재: 확인 가능]\n\n[공급·이송 계약 포인터: 범위 제한 확인 가능]\n\n[구형 연속성·서비스 계층: 일부 확인]\n\n그 아래 보이지 않는 것도 명시됐다.\n\n[비동의 개인 과거사: 비공개]\n\n[환자 삭제요청 로컬 원시조각: 통상 접근 불가]\n\n[외부 사본 제한요청: 결과 미확정]\n\n[연결된 다수 환자 식별자: 공개 불가]''', '''[허용 범위: 동의된 과정증명 / 선택 환자의 현재 임상존재 / 제한된 공급·이송 포인터 / 구형 연속성·서비스 계층 일부]\n\n그 아래 비허용·미확정 범위도 한 줄로 명시됐다.\n\n[비허용·미확정: 비동의 개인 과거사 / 삭제요청 로컬 원시조각 / 외부 사본 제한결과 / 연결 환자 식별자]''')

# Ensure key direct machine clues remain.
checks={
 '043-돌려받지-않는-코어-v1.md':['[OPERATOR: UNREGISTERED]','[STATE: MISMATCH]'],
 '044-다시-조립된-07호-v1.md':['[COOLING DISTRIBUTION DELAY]','[OPERATOR STATE: MISMATCH]'],
 '065-죽은-사람에게-필요한-약-v1.md':['72시간 안에 적극 소모품/지원이 필요한 환자: 23명.','현재 재고로 완전 프로토콜 사이클 보장 가능: 11명분.']
}
for fn,needles in checks.items():
    t=(ROOT/fn).read_text(encoding='utf-8')
    for needle in needles:
        if needle not in t: raise SystemExit(f'{fn}: required clue lost: {needle}')

print('UI cluster cleanup applied safely')
