import sys

sys.stdin = open("25304.txt", "r")

final = int(input())

N = int(input())
sum_ = 0
for _ in range(N):
    cost, num = map(int, input().split())
    sum_ += cost * num

if final == sum_:
    print('Yes')
else:
    print('No')

