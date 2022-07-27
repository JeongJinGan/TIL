# https://www.acmicpc.net/problem/2851
import sys

sys.stdin = open("2851_슈퍼마리오.txt", "r")

mush_ = [] # 10개의 버섯을 담을 공간
score = 0 # 점수 0으로 초기화
for i in range(10):
    mush_.append(int(input()))

for j in mush_:
    score += j  # mush_에 담은 버섯을 한개씩 누적해서 더해준다.
    if score >= 100:    # 만약 누적점수가 100점 이상이라면
        if score - 100 > 100 - (score - j): # 100점 과의 차이가 , 누적 점수 100점 이상 일때의 점수 > 누점 100점 전의 점수보다 크다면
            score -= j # 누점 100점 전의 점수
        break
print(score)
