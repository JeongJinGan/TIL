from os import name
import sys

sys.stdin = open("1436.txt", "r")

N = int(input())

cnt = 0
n = 1

while True:
    n += 1
    if '666' in str(n):
        cnt += 1
    if cnt == N:
        print(n)
        break



