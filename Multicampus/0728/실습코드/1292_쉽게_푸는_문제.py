# https://www.acmicpc.net/problem/1292
import sys

sys.stdin = open("1292_쉽게_푸는_문제.txt", "r")

A, B = map(int, input().split())
data_ = [0] 
sum = 0
for i in range(1, B+1): # 1부터 입력받은 숫자 중 큰 숫자까지
    for j in range(i):  # 2중 for문으로 1일때는 1번 2일때는 2번 3일때는 3번 ...
        data_.append(i) # data_에 넣는다
# print(data_)
for i in range(A, B+1): # 입력받은 숫자 사이에 값들을 순회
    sum += data_[i] # sum에 누적
print(sum)