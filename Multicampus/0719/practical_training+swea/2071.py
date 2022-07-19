import sys

sys.stdin = open("2071_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    avg = round(sum(numbers)/10)
    print(f'#{test_case} {avg}')