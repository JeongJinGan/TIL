# https://www.acmicpc.net/problem/3052
import sys

sys.stdin = open("3052_나머지.txt", "r")
rest_ = []
for i in range(1, 11):
    num = int(input())
    rest_.append(num % 42)
rest_ = set(rest_)
# print(rest_)
print(len(rest_))      


