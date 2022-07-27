# https://www.acmicpc.net/problem/1157
import sys

sys.stdin = open("1157_단어공부.txt", "r")

word = input().upper()  # 출력을 대문자로 할거니까 입력받은 값을 전부 대문자로 변경
list_word = list(set(word)) # 입력받은 문자를 하나씩 list에 넣기

cnt_list_ = [] # 각각의 문자의 개수 카운트 할 리스트

for i in list_word:
    cnt = word.count(i) # 받은 문자열 count
    # print(cnt)
    cnt_list_.append(cnt) # [1, 1, 4, 4]
    # print(cnt_list_)

if cnt_list_.count(max(cnt_list_)) >= 2:    # cnt_list_에 가장높은 숫자의 개수가 2개 이상이라면
    print('?')  # ?를 출력
else:
    print(list_word[(cnt_list_.index(max(cnt_list_)))]) # 아니라면 입력받은 문자 각각의 리스트의 카운트 리스트의 최고값의 인덱스를 출력

