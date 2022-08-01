# 문제를 제대로 읽지 않고 개수만 맞추려고 했을 때
# T = int(input())
# list_ = []
# for _ in range(T):
#     ps = input()
#     ls = list(ps)

#     sum1 = ls.count('(')
#     sum2 = ls.count(')')
#     if sum1 == sum2:
#         list_.append('Yes')
#     else:
#         list_.append('No')

# for i in list_:
#     print(i)


import sys

sys.stdin = open("9012_괄호.txt", "r")

T = int(input())
list_ = []
for i in range(T):
    ps = input()
    stack = list(ps)

    sum = 0
    for j in stack:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            list_.append('NO')
            break
    if sum > 0:
        list_.append('NO')
    elif sum == 0:
        list_.append('YES')

for i in list_:
    print(i)