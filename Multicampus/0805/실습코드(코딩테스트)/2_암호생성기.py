import sys

sys.stdin = open("_암호생성기.txt")

T = 10

for tc in range(T):
    t_c = int(input())
    queue = list(map(int, input().split()))

    i = 1
    while True:
        # 한 사이클(최대 5감소)
        if i > 5:
            i = 1
        cycle_ = queue.pop(0) - i # 0번째 인덱스의 값 -i
        # 값이 0보다 작거나 같으면 0 append 해준 뒤 break
        if cycle_ <= 0:
            queue.append(0)
            break
        queue.append(cycle_) # 인덱스트이 -i 한거 다시 append
        i += 1 # i 증가
    print(f'#{t_c}', *queue)
        