import sys

sys.stdin = open("_Flatten.txt")

for _ in range(10):
    dumb_num = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dumb_num): # 주어진 덤프 횟수 만큼 반복
        max_ = max(boxes) # 반복할때마다 boxes안에 max값 저장
        min_ = min(boxes) # 반복할때마다 boxes안에 min값 저장
        # print(max_)
        i_max_ = boxes.index(max_) # 저장한 max 값에 인덱스 찾아서 저장
        i_min_ = boxes.index(min_) # 저장한 min 값에 인덱스 찾아서 저장

        boxes[i_max_] -= 1 # max 더미 -1
        boxes[i_min_] += 1 # min 더미 + 1

    print(f'#{_ + 1} {max(boxes) - min(boxes)}')



