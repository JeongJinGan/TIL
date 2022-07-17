# 파일명, 어떤 모드로 열지,
# 인코딩을 설정
with open('students.txt','r',encoding='utf-8') as f:
    # 텍스트는 string 타입
    text = f.read()
    print(text)
    # string.split() => list 타입
    names = text.split()
    cnt = 0
    for name in names:
        # name : 첫번째 시행 - 아이유
        # 언제? 김씨?
        if name.startswith('김'):
        # if name[0] == '김':
            cnt += 1
    print(f'김씨는 총 {cnt}명 입니다.')        