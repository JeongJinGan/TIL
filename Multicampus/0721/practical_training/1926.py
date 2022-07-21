import sys

sys.stdin = open("1926_input.txt", "r")

T = int(input())
for i in range(1, T+1):
    a = i//10
    b = i%10
    if a == 3 or a == 6 or a == 9: # i를 10으로 나눈 몫의 값이 3,6,9일때
        if b == 3 or b == 6 or b == 9: # i를 10으로 나눈 나머지의 값이 3,6,9일때
            print("-- ",end='')
            continue
        print("- ",end='')

    elif b == 3 or b == 6 or b == 9:
        print("- ",end='')
    else:
        print(f'{i}',end=' ')
