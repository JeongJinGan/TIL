import sys

sys.stdin = open("_최빈수구하기.txt", "r")


T = int(input()) # 전체 테스트 케이스의 수 입력받기
for test_case in range(T):
    caseN = int(input()) # 케이스 번호 입력받기
    scores = list(map(int, input().split())) # 점수 케이스 별로 100개씩 받기
    score_num = [0] * 101 # 점수별 체크 리스트 

    for j in scores: # 입력받은 점수 리스트 순회
        score_num[j] += 1 # 리스트 인덱스 번호에 순회 한 숫자 + 1 누적

    max_score = 0 # 최고 점수 0 초기화

    for k in range(0, len(score_num)): # 점수별 체크 리스트 순회
        if score_num[k] >= max_score: # 하나씩 비교
            max_index = k # 가장많은 값을 가지고 있는 인덱스 저장
            max_score = score_num[k] # 하나씩 비교하면서 많은 값 가지고 있는 인덱스의 값을 저장
    print(f'#{caseN} {max_index}')