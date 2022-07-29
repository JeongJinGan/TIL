import sys

sys.stdin = open("_직사각형길이찾기.txt", 'r')

T = int(input()) # 전체 테스트 케이스의 수 입력받기
for test_case in range(T):
    lengths_ = list(map(int, input().split())) # 사각형의 3변의 길이 입력받기

    length_ = 0 # 알아내야할 나머지 길이 0으로 초기화
    if lengths_.count(lengths_[0]) == 3: # 만약 입력받은 사각형의 변의 길이 리스트 첫번째값이 3개가 있다면
        length_ = lengths_[0] # 나머지 변의 길이도 동일
    else:
        if lengths_.count(max(lengths_)) == 1: # 입력받은 사각형의 변의 길이 중 최고 숫자가 1개라면
            length_ = max(lengths_) # 나머지 변의 길이도 최고 숫자와 동일
        else:
            length_ = min(lengths_) # 그게 아니라면 나머지 변의 길이(min) = 구해야할 나머지 변의 길이

    print(f'#{test_case + 1} {length_}')