import sys

sys.stdin = open("_괄호짝짓기.txt")

# 스택을 이용
for tc in range(10):
    N = int(input())
    list_ = list(input())
    stack_ = list()

    # 왼쪽 괄호
    left = ['(', '{', '[', '<']
    # 오른쪽 괄호
    right = [')', '}', ']', '>']

    # N 순회
    for i in range(N): 
        if list_[i] in left: # 입력받은 문자[i]번째가 left에 있다면
            stack_.append(list_[i]) # 스택에 넣기

        if list_[i] in right: # 입력받은 문자[i]번째가 left에 있다면
            # 스택에 첫번째 괄호랑 쌍이라면
            if right.index(list_[i]) == left.index(stack_[-1]):
                stack_.pop() # 스택에서 제거
            else: # 아니라면 break
                break  
    
    result = 0
    if len(stack_) == 0: # 제거를 다 해서 길이가 0이라면
        result = 1 # 결과값이 1

    print(f'#{tc+1} {result}')


# 무조건 왼쪽 괄호 부터 입력이 되고 개수만 맞으면 될 거 같아 주먹구구식 방법으로 해결
# for tc in range(10):
#     N = int(input())
#     list_ = list(input())

#     sum1 = list_.count('(')
#     sum2 = list_.count(')')
#     sum3 = list_.count('{')
#     sum4 = list_.count('}')
#     sum5 = list_.count('[')
#     sum6 = list_.count(']')
#     sum7 = list_.count('<')
#     sum8 = list_.count('>')
#     res = 0
#     if sum1 == sum2 and sum3 == sum4 and sum5 == sum6 and sum7 == sum8:
#         res = 1
#     else:
#         rse = 0

#     print(f'#{tc+1} {res}')
