# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("2953_나는요리사다.txt", "r")

list_ = []
for i in range(1, 6):
    list_.append(sum(map(int, input().split())))
print(list_.index(max(list_))+1,max(list_))