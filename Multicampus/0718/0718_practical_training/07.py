# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count를 for문안에 넣어놓지 않아서 1개씩 진행될때마다 
# 추가해주지 못한다.
# print문의 //연산자는 소수점 이하를 버리기 때문에 /나누기로 출력
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1
print(total / count)