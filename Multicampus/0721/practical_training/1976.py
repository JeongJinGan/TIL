import sys

sys.stdin = open("1976_input.txt", "r")

T = int(input())
for i in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h3 = h1 + h2
    m3 = m1 + m2
    if h3 > 12:
        h3 = h3 - 12
    if m3 > 59:
        h3 +=1
        m3 = m3 - 60
    
    print(f'#{i} {h3} {m3}')