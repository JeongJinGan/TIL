import sys

sys.stdin = open("1284_input.txt", "r")

T = int(input())
mim = 0
for i in range(1, T+1):
    p,q,r,s,w = map(int, input().split())
    a = p*w

    if w < r:
        b = q
    else:
        b = q + (w-r)*s

    # print(f'#{i} {min(a,b)}')   -> min()사용하면 밑에 코드까지 작성 안해도된다.    
      
    if a < b:
        min = a

    else:
        min = b

    print(f'#{i} {min}')