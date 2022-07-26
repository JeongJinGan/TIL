T = int(input())
# 실수로든 어떻든 O,X를 소문자로 쓸 수 있기 때문에
# O,X를 변수에 넣는다.
# 변수에 안넣고 사용하면 코드가 틀렸다고 나올 시 알 수가 없다.
O = 'O' 
X = 'X'

for i in range(T):
    OX = input()

    count_O = 1 # 연속된 O의 개수
    sum_ = 0 # 점수의 총합

    for answer in OX:
        if answer == O:
            count_O += 1 # 연속된 O의 개수 1증가
            sum_ = count_O + sum_
        if answer == X:
            count_O = 0 # 연속된 O의 개수를 초기화

    print(sum)

