import sys

sys.stdin = open("23253_자료구조는_정말_최고야.txt", "r")

# N, M = map(int, input().split())
# ASC_possible = True

# for _ in range(M):
#     k1 = int(input())
#     k2 = list(map(int, input().split()))
    
#     if k2 != sorted(k2, reverse=True):
#         ASC_possible = False
#         break

# if ASC_possible:
#     print('Yes')
# else:
#     print('No')

N, M = map(int, input().split())
ASC_possible = True

for _ in range(M):
    k1 = int(input())
    k2 = list(map(int, input().split()))
    
    for i in range(k1 - 1):
        if k2[i] < k2[i+1]:
            ASC_possible = False
            break
    
    if not ASC_possible:
        break

if ASC_possible:
    print('Yes')
else:
    print('No')