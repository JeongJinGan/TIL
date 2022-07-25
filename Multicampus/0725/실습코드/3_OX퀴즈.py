# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt", "r")

test_case = int(input())
for i in range(test_case):
    ox = input()
    l_ox = list(ox) # 하나씩 확인위해 리스트에 넣음
    sum = 0 # ox 결과 0으로 초기화
    cnt = 1 # o일때 1부터 시작
    for j in l_ox:
        if j == 'O':
            sum += cnt # O를 만날때 cnt를 sum에 더해주기
            cnt += 1 # cnt + 1
        else:
            cnt = 1 # x를 만날때 cnt 1로 변경
    print(sum)        
