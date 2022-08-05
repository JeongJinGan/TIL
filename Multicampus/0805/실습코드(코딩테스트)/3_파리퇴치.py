import sys

sys.stdin = open("_파리퇴치.txt")


T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # N = 배열크기, M = 파리채크기
    matrix = [list(map(int, input().split())) for _ in range(N)]

    sum_max = 0
    # 파리채를 배열안에서 최대로 내리칠 수 있는 길이
    for i in range(N-M+1): 
        for j in range(N-M+1): 
            cnt = 0

            # 파리채 크기만큼 순회
            for k in range(M): 
                for p in range(M):
                    # M*M 범위 내의 해당 인덱스의 합을 저장
                    cnt += matrix[i+k][j+p]
            # 최대값 비교 후 저장
            if cnt > sum_max:
                sum_max = cnt
    print(f'#{_+1} {sum_max}')
