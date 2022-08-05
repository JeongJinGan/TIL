import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for _ in range(T):
    N, K = map(int, input().split()) # 배열의 크기와 들어갈 수 있는 단어의 길이
    matrix = [list(map(int,input().split())) for _ in range(N)] # N크기의 배열 만들기
    ok_ = 0

    # 행 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 0: # 행부터 차례대로 순회 중 값이 0 이라면
                if cnt == K: # cnt의 값이 K(들어갈 수 있는 단어의 길이)랑 같다면
                    ok_ += 1 # ok_라는 변수에 + 1
                cnt = 0 # cnt다시 초기화
            else:
                cnt += 1 # 0이 아니라면 cnt + 1
        if cnt == K: # 0을 만나지 않았지만 cnt가 K와 같다면
            ok_ += 1 # ok_ 변수에 1증가
    
    # 열 확인(행과 같은 방식으로 순회)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[j][i] == 0:
                if cnt == K:
                    ok_ += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            ok_ += 1
    
    print(f'#{_+1} {ok_}')

