# https://www.acmicpc.net/problem/5622
import sys

sys.stdin = open("5622_다이얼.txt", "r")

daieol = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
call = input()
sum = 0
for i in range(len(call)):
    for j in daieol:
        if call[i] in j:
            sum += daieol.index(j)+3

print(sum)