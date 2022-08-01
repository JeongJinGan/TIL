import sys

sys.stdin = open("2161_카드.txt", "r")

N = int(input())

queue = list(range(1, N + 1)) # 큐로 리스트 생성(1~N까지)

while len(queue) > 1: # 큐의 길이가 1보다 클때까지 무한반복
    print(queue.pop(0), end =' ') # 첫번째 인덱스의 값을 빼고 출력
    queue.append(queue.pop(0)) # 빼고 난뒤의 첫번째 인덱스를 pop 한 뒤 맨 뒤로 append

print(*queue)


# 덱을 이용한 풀이
# from collections import deque

# N = int(input())
# queue = deque(range(1, N + 1))

# while len(queue) > 1:
#     print(queue.popleft(), end = ' ')
#     queue.append(queue.popleft())

# print(queue[0])