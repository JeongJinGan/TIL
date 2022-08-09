import sys

sys.stdin = open("2897.txt", "r")

N, M = map(int, input().split())

matrix = [input() for _ in range(N)]
# print(matrix)
zero, one, two, three, four = 0, 0, 0, 0, 0
for i in range(N-1):
    for j in range(M-1):
        # (#) - 빌딩, (X) - 주차 된 차
        
        stand = matrix[i][j]
        right = matrix[i][j+1]
        under = matrix[i+1][j]
        rigdia = matrix[i+1][j+1]

        park_area = stand + right + under + rigdia

        if '#' in park_area:
            continue
        else:
            broke_car = park_area.count('X')
            if broke_car == 0:
                zero += 1
            elif broke_car == 1:
                one += 1
            elif broke_car == 2:
                two += 1
            elif broke_car == 3:
                three += 1
            else:
                four +=1

print(zero)
print(one)
print(two)
print(three)
print(four)

