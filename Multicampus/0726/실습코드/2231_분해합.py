# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("2231_분해합.txt", "r")
N = int(input())
ans = 0
for i in range(1, N+1):
    list_ = list(map(int, str(i))) # 1부터 입력받은 숫자까지 리스트로 변환
    # ex) N이 216이라면 (일의자리)[1]~[9]~(십의자리)[1,0]~[9,9]~(백의자리)[1,0,0]~[2,1,6]까지
    ans = i + sum(list_) # i도 1~입력받은숫자까지 순회하는데, 
    if ans == N: # i + list_의 합이 = 입력받은 숫자(N)이라면
        print(i)
        break
    if i == N: # 생성자가 없다면
        print(0)   