# https://www.acmicpc.net/problem/2609
# 런타임에러
# maxi, mini = map(int, input().split()) # 두 개의 자연수 입력받기
# list_ = [] # 공약수 리스트 초기화
# for i in range(2, min(maxi, mini) + 1): # 2부터 입력받은 두 수중 작은숫자까지 for문
#     if maxi % i == 0 and mini % i == 0: # 2부터 ~ 두 개의 입력받은 자연수랑 나눴을 때 나머지가 0인것을
#         list_.append(i) # 리스트에 넣어준다.
# m_list = max(list_) # 리스트 중 제일 큰 숫자가 입력받은 두 수의 최대 공약수

# print(m_list)
# print(m_list * (maxi // m_list) * (mini // m_list)) # 최소 공배수 = 최대공약수 * 입력받은 숫자를 최대공약수로 나누었을때의 몫

# 유클리드 호제법 (파이썬 내장함수)
# import math
# maxi, mini = map(int, input().split())
# print(math.gcd(maxi,mini))
# print(math.lcm(maxi,mini))
import sys

sys.stdin = open("2609_최대공약수와_최소공배수.txt", "r")
num1, num2 = map(int, input().split())
n1, n2 = num1, num2 # while문을 돌릴때 num1,num2 값이 바뀌기 때문에 따로 다시 저장
while num2 > 0: # 두번째로 입력받은 숫자가 0보다 클때까지
    num1, num2 = num2, num1 % num2 # 두번째 입력값을 첫번째로 바꾸고 두번째 값을 첫번째 나누기 두번째값의 몫
maxi = num1 # 마지막으로 나눈 값의 몫을 maxi에 저장
print(maxi)
print(maxi * (n1//maxi) * (n2//maxi)) # 최대공약수 * 각각의 입력값 나누기 최대공약수의 몫


