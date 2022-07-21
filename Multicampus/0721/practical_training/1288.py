import sys

sys.stdin = open("1288_input.txt", "r")

# T = int(input())

# for i in range(1, T+1):
#     a = int(input())
#     list = [0] * 10
#     cnt = 1 
#     # 입력받은 a에 cnt(1부터 증가) 곱해주기
#     while 0 in list:
#         num = str(a * cnt)
#         for j in range(len(num)):
#             list[int(num[j])] +=1
#         cnt += 1
#     print(f'#{i} {num}')

# set() 으로 풀어보기
T = int(input())
for test_case in range(1, T + 1):
    # input 가져오기
    N = int(input())
    N1 = N
    # set에 계속 추가 예정
    numbers = set()
    # while 반복 => set 길이가 10이 될 때까지
    while True:
        # for 반복 : 숫자를 문자로
        for n in str(N):       
        # numbers set에 추가
            numbers.add(n)
        if len(numbers) == 10:
            break
        # print(n, numbers)
        N += N1
    #print(N)    
    print(f'#{test_case} {N}')



