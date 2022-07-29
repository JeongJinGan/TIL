import sys

sys.stdin = open("_암호문1.txt", 'r')

list_ = []

o_length = int(input()) # 원본 암호문의 길이
o_secret_ = list(map(int, input().split())) # 원본 암호문
command_num = int(input()) # 명령어의 개수

for i in range(command_num): # 명령어의 개수 만큼
    del_ = input() # I 입력 받기 (이게 안되네)
    print(del_)
    y = int(input()) # y값(숫자 삽입) 입력 받기
    s = int(input()) # s값(덧붙일 숫자) 입력 받기
 
    for j in s:
        command_ = list(input().split())
    
    for k in j-s:
        list_.append(command_[k])

for f in range(10):
    print(command_.get(f))