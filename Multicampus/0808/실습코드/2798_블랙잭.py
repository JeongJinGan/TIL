import sys

sys.stdin = open("2798.txt", "r")

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0

for i in range(len(cards)):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
                result = max(result, cards[i] + cards[j] + cards[k]) # 파이썬 내장함수 result와 뒤에 수를 비교하여 최대값 출력
                
print(result)


