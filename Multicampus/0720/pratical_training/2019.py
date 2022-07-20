import sys

sys.stdin = open("2019_input.txt", "r")

a = int(input())
num = int(0)
while num<=a:
    print(int(2)**num ,end=' ')
    num+=1