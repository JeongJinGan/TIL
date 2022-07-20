import sys

sys.stdin = open("1933_input.txt", "r")

T = int(input())
for i in range(1, T+1):
    if T % i == 0:
        print(i, end=' ')