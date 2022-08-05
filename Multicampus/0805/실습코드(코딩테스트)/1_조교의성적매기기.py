import sys

sys.stdin = open("_조교의성적매기기.txt")

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for _ in range(T):
    N ,k = map(int, input().split())

    list_ = []

    for i in range(N):
        mid, final, project = map(int, input().split())
        sum_ = (mid * 0.35) + (final * 0.45) + (project * 0.2)
        list_.append(sum_)
    # print(list_)

    k_score = list_[k-1]
    list_.sort(reverse=True) # 성적은 높은 순 부터
    
    # 10명 동일점수
    rank = N // 10
    score = list_.index(k_score) // rank

    print(f'#{_+1} {grade[score]}')

