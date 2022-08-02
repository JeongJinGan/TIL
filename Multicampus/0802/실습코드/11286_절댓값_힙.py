import sys
import heapq

sys.stdin = open("11286.txt", "r")



heap = []

for _ in range(int(input())):
    n = int(sys.stdin.readline())

    if n != 0:
        # (abs(n), n) heapq는 첫번째 요소를 기준으로 정렬하므로 첫번째 우선순위, 두번째에 원래 값
        heapq.heappush(heap, (abs(n), n)) 
        # print(heap)
    else:
        # heap 리스트의 길이가 0 이라면
        if len(heap) == 0:
            print(0) # 0 출력
        else:
            print(heapq.heappop(heap)[1])
            # (1, -1)
            # (1, 1)
            # (2, -2)
            # (2, 2)
            # 이런식으로 있을 때 첫번째 값 출력