import sys

sys.stdin = open("_신용카드만들기1.txt", 'r')


T = int(input()) # 전체 테스트 케이스의 수 입력받기
for test_case in range(T):
    nums_ = list(map(int, input().split()))
    even_sum = 0
    odd_sum = 0
    for i in range(0, 15):   
        if i % 2 == 0:  # 인덱스번호 나누기 2를 했을때 나머지가 0이 나온다면
            odd_sum += nums_[i] * 2 # 해당 인덱스 누적해서 (값 * 2)      
        else:
            even_sum += nums_[i] # 아니라면, 누적해서 더해준다         
    x =  ((even_sum + odd_sum) // 10 + 1) * 10 # 인덱스 짝수,홀수 계산법해서 더한 결과를 10으로 나눈 (몫 + 1) * 10
    x -= even_sum + odd_sum # 10의 배수로 만든다음 계산한값을 빼면 16번째의 값이 나온다
    if x == 10: # 만약 16번째 값이 10이 나온다면
        x = 0 # 0으로 변환
    print(f'#{test_case + 1} {x}')
