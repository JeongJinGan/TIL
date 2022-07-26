# https://www.acmicpc.net/problem/2846
import sys

sys.stdin = open("2846_오르막길.txt", "r")

height = int(input())
way = list(map(int, input().split()))
cnt = 0
list_ = []
for i in range(1, height): # i는 1부터 입력받은 숫자까지
    if way[i] > way[i-1]: 
        cnt += way[i] - way[i-1]
        if i == height-1:
            list_.append(cnt)
    else:
        list_.append(cnt)
        cnt = 0
# print(list_)
print(max(list_)) 

# 예제입력 1
# i = 1 일때 cnt = cnt + 1 ==> cnt = 0 + 1 = 1
# i = 2 일때 else라서 cnt = 1 append해주고 cnt = 0 으로
# i = 3 일때 cnt = cnt + 3 ==> cnt = 0 + 3 = 3
# i = 4 일때 cnt = cnt + 2 ==> cnt = 3 + 2 = 5 
# i == height-1 에 들어와서 마지막 cnt값 list_에 append 해주기 
    