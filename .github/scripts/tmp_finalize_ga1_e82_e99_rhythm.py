from pathlib import Path
import re
ROOT=Path('manuscript/ga1')

def rep(fn,old,new):
    p=ROOT/fn
    t=p.read_text(encoding='utf-8')
    n=t.count(old)
    if n!=1: raise SystemExit(f'{fn}: expected block once, got {n}: {old[:70]!r}')
    p.write_text(t.replace(old,new,1),encoding='utf-8')

f='082-다섯-개의-문-v1.md'
rep(f,'''그날 밤 하렌이 표를 다시 만들었다.\n\n이번에는 다섯 패키지가 세로축이 아니었다.\n\n기능이 세로축이었다.\n\n전력·식량.\n\n급여·고용.\n\n의료.\n\n보안.\n\n교육.\n\n정비.\n\n신원·기록.\n\n이송·탈퇴.''','''그날 밤 하렌은 표를 다시 만들었다. 이번에는 다섯 패키지가 아니라 기능을 세로축에 놓았다. 전력·식량, 급여·고용, 의료, 보안, 교육, 정비, 신원·기록, 이송·탈퇴였다.''')
rep(f,'''30.2%.\n\n23.0%.\n\n17.3%.\n\n12.6%.\n\n9.5%.\n\n7.4%.''','''수치는 30.2%, 23.0%, 17.3%, 12.6%, 9.5%, 7.4%로 흩어졌다.''')
rep(f,'''리안은 여전히 하나를 고르고 싶었다.\n\n그게 자신의 습관이었다.\n\n전투에서 다섯 항로가 있으면 하나를 고른다.\n\n자원을 분산하면 모두 죽는 상황이 있다.''','''리안은 여전히 하나를 고르고 싶었다. 전투에서 다섯 항로가 있으면 하나를 고르는 게 그의 습관이었고, 실제로 자원을 분산하면 모두 죽는 상황도 있었다.''')

f='099-살아남은-학교의-청구서-v1.md'
rep(f,'''강제이송이 원인이라는 주장.\n\n저항방해가 원인이라는 주장.\n\n낡은 설비와 상충명령이 원인이라는 기술감사.\n\n현장대응 지연.\n\n모두 기록됐다.''','''강제이송이 원인이라는 주장과 저항방해가 원인이라는 주장, 낡은 설비·상충명령을 지목한 기술감사, 현장대응 지연까지 서로 지워지지 않은 채 기록됐다.''')
rep(f,'''대부분 쓸모없는 오래된 부품이었다.\n\n중계 안테나.\n\n구식 서비스 커플러.\n\n압력문 액추에이터.\n\n폐기된 프레임 고정구.''','''대부분은 중계 안테나, 구식 서비스 커플러, 압력문 액추에이터, 폐기된 프레임 고정구 같은 오래된 부품이었다.''')
rep(f,'''그리고 오래된 서비스 식별문자열.\n\n완전한 키는 아니었다.\n\n그런데 일부 패턴이 익숙했다.\n\n07호.\n\n블랙 워드.\n\nORA-3.\n\n중앙키에서 봤던 비상서비스 계보.''','''그 아래에는 오래된 서비스 식별문자열도 있었다. 완전한 키는 아니었지만 일부 패턴이 07호, 블랙 워드, ORA-3와 중앙키에서 확인한 비상서비스 계보와 닮아 있었다.''')
rep(f,'''세린이 화면을 당겼다.\n\n인양 출처.\n\n자매선.\n\n상태.''','''세린은 화면을 당겨 인양 출처와 자매선, 상태 항목을 한꺼번에 확인했다.''')

# No reader-facing production episode refs or retired name introduced in the touched files.
for fn in ['082-다섯-개의-문-v1.md','099-살아남은-학교의-청구서-v1.md']:
    t=(ROOT/fn).read_text(encoding='utf-8'); body=t[t.find('# 제'):]
    if '리안 카르도' in body: raise SystemExit(f'{fn}: retired protagonist name')

print('targeted rhythm cleanup applied')
