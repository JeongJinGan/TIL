import sys

sys.stdin = open("2050_input.txt", "r")

a = input()
for i in a:
    print(ord(i)-64, end=' ')