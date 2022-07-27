# https://www.acmicpc.net/problem/2941
import sys

sys.stdin = open("2941_크로아티아_알파벳.txt", "r")

c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳 
alpha = input() # 문자열 입력받기

for i in c_alpha:   # 크로아티아 알파벳 하나씩 순회
    alpha = alpha.replace(i, 'c')   # 입력받은 문자열중에 크로아티아 알파벳 있으면 C로 치환
print(len(alpha)) # 크로아티아 알파벳이 있으면 c로 치환 뒤 전체 길이 출력