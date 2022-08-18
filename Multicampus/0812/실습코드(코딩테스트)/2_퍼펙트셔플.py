import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for _ in range(T):
    cards_num = int(input())
    cards = list(input().split())

    div_front = 0
    div_back = (cards_num + 1) // 2 # 절반으로 나누고 나눈 것들에 두번째 카드 시작 번호
    list_ = []
    
    for i in range(cards_num // 2):
        list_.append(cards[div_front])
        list_.append(cards[div_back])
        div_front += 1
        div_back += 1

    if cards_num % 2 == 1: # 카드에 개수가 홀수라면 가운데 카드를 맨 마지막으로
        list_.append(cards[cards_num // 2])

    print(f'#{_ + 1}', end= ' ')
    print(*list_)

