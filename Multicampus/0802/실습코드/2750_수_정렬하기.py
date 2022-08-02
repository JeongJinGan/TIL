import sys
import heapq
sys.stdin = open("2750.txt", "r")

N = int(input())
list_ = []
for _ in range(N):
    n = int(input())
    list_.append(n)

list_ = sorted(list_)
for i in range(len(list_)):
    print(list_[i])


heap = []
for i in range(int(input())):
    n = int(sys.stdin.readline()) 
    heapq.heappush(heap, n)
    
while heap:
    print(heapq.heappop(heap))
