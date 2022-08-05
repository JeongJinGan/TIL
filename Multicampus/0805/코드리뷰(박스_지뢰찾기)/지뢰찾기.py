import sys

sys.stdin = open("지뢰찾기.txt")

def pprint(list_):
    for row in list_:
        print(row)

# 
# 8방위 델타리스트
델타_y = [-1, -1, -1, 0, 0, 1, 1, 1]
델타_x = [-1, 0, 1, -1, 1, -1, 0, 1]

지뢰 = "*"
빈공간 = "."

n = 8
# 게임보드 = [
#     "...**..*",
#     "......*.",
#     "....*...",
#     "........",
#     "........",
#     ".....*..",
#     "...**.*.",
#     ".....*..",
# ]
# 오픈보드 = [
#     "xxxx....",
#     "xxxx....",
#     "xxxx....",
#     "xxxxx...",
#     "xxxxx...",
#     "xxxxx...",
#     "xxx.....",
#     "xxxxx...",
# ]

n = int(input())
게임보드 = []
for _ in range(n):
    게임보드.append(list(input()))
    
오픈보드 = []
for _ in range(n):
    오픈보드.append(list(input()))

# 결과보드 생성
결과보드 = []
for i in range(n):
    temp = ["."] * n
    결과보드.append(temp)
# pprint(결과보드)


게임보드 = list(게임보드)
오픈보드 = list(오픈보드)
지뢰_발견 = False

# 이중반복문
for y in range(n):
    for x in range(n):
        # 현재 위치가 오픈한 위치
        # 오픈보드 -> x
        if 오픈보드[y][x] == "x":
            지뢰수 = 0
            for d in range(8):
                탐색_y = y + 델타_y[d]
                탐색_x = x + 델타_x[d]
                # 탐색_y 탐색_x의 범위는 리스트를 벗어나면 안된다.
                # 리스트의 범위는 0 ~ 7(리스트의 길이 8)

                if 0 <= 탐색_y <= n-1 and 0<= 탐색_x <= n-1:
                    if 게임보드[탐색_y][탐색_x] == 지뢰:
                        지뢰수 += 1

            결과보드[y][x] = str(지뢰수)
            
            # 현재 오픈한 위치에 지뢰가 있는지 확인 
            if 게임보드[y][x] == 지뢰:
                지뢰_발견 = True

# 지뢰를 발견했으면 모든 지뢰의 위치를 결과보드에 표시
if 지뢰_발견 == True:
    for y in range(n):
        for x in range(n):
            if 게임보드[y][x] == 지뢰:
                결과보드[y][x] = 지뢰

# pprint(결과보드)
for row in 결과보드:
    print("".join(row))