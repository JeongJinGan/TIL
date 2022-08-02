import sys

sys.stdin = open("1269.txt", "r")

A, B = map(int, input().split())
AS = list(map(int, input().split()))
BS = list(map(int, input().split()))

A_B = set(AS) - set(BS)
B_A = set(BS) - set(AS)
print(len(A_B) + len(B_A))