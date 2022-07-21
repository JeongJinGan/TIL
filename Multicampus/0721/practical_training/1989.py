import sys

sys.stdin = open("1989_input.txt", "r")

T = int(input())
for i in range(1,T+1):
    s = input()
    if s == s[::-1]: # s(처음문자~끝문자) == s[::-1](끝문자~처음문자) 
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')



