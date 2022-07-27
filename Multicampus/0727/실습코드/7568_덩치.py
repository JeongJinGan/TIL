# https://www.acmicpc.net/problem/7568
import sys

sys.stdin = open("7568_덩치.txt", "r")
N = int(input())
people = []

for i in range(N):
    weight, height = map(int, input().split()) # 몸무게와 키를 순차적으로 입력받는다
    people.append((weight, height))

for j in people:
    rank = 1

    for k in people:
        if(j[0] != k[0] & (j[1] != k[1])):  
            if (j[0] < k[0]) & (j[1] < k[1]):
                rank += 1

    print(rank,end=' ')