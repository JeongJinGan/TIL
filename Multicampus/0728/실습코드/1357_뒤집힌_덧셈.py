# https://www.acmicpc.net/problem/1357
import sys

sys.stdin = open("1357_뒤집힌_덧셈.txt", "r")

X, Y = input().split()
Rev = str(int(X[::-1]) + int(Y[::-1]))
print(int(Rev[::-1]))

# 123 100
# 321 001
# 322
# 223
