import sys

sys.stdin = open("_소득불균형.txt", 'r')

T = int(input())    # 전체 테스트 케이스의 수 입력받기

for test_case in range(T):
    case_num = int(input()) # n 번째 테스트 케이스
    gets_ = list(map(int, input().split())) # 수입을 리스트 형태로 입력 받는다
    avgs_ = (sum(gets_) // len(gets_)) # 입력받은 수입을 합하고 그 리스트 길이 만큼 나눈다

    under_avg = 0
    for get in gets_:   # n 번째 테스트 케이스 입력받은 리스트를 순회
        if get <= avgs_: # 만약, 입력받은 수입이 평균보다 낮거나 같으면
            under_avg += 1  # +1 을 해준다

    print(f'#{test_case + 1} {under_avg}')