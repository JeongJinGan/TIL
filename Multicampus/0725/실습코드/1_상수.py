# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt", "r")

num1, num2 = input().split()
a_num1 = num1[::-1] # 입력받은 숫자 반대로
a_num2 = num2[::-1] # 입력받은 숫자 반대로
if a_num1 > a_num2: # 반대로 된 숫자들 비교
    print(a_num1)
else:
    print(a_num2)    