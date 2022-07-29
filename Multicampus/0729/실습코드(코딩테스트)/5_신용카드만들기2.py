import sys

sys.stdin = open("_신용카드만들기2.txt", 'r')

list_ = ['3','4','5','6','9']
T = int(input()) # 전체 테스트 케이스의 수 입력받기
for test_case in range(T):
    card_nums_ = list(input().split())
    
    for card_num in card_nums_: # 리스트의 문자들을 하나씩 순회
        if card_num[0] in list_ and len(card_num) > 15: # 리스트에 첫번째 문자가 list_ 안에 있나 그리고 문자열이 16 이상인가
            print(f'#{test_case + 1} 1') # 맞다면 1을 출력
        else:
            print(f'#{test_case + 1} 0') # 아니라면 0을 출력