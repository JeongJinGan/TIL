import sys

sys.stdin = open("_민석이의과제체크하기.txt")
# 과제를 안한 사람 체크 리스트를 여기에 선언했더니 초기화가 되지 않는다.
# n_student = [] 
T = int(input())
for _ in range(T):
    N, K = map(int, input().split()) # 수강생, 과제제출 인원 입력 받기
    list_ = list(map(int, input().split())) # 과제제출 인원 번호 입력 받음과 동시에 리스트에 넣기
    n_student = [] # 과제안한 인원 체크 리스트

    for i in range(1, N+1): # 1 ~ N까지(N포함)
        if i not in list_: # 1 ~ N 순회하면서 과제제출 인원에 없는 사람
            n_student.append(i) # n_student에 넣기
    print(f'#{_+1}', *n_student)

