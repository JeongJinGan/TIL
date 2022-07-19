import sys

sys.stdin = open("2029_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    share = a//b
    rest = a%b
    print(f"#{test_case} {share} {rest} ")