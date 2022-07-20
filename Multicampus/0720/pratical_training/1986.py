import sys

sys.stdin = open("1986_input.txt", "r")

T = int(input())
for i in range(1, T+1):
    a = int(input())
    if a%2 == 1:
        a = a//2+1
    else:
        a = a//-2
    print(f'#{i} {a}')