# 숫자 입력을 받아서 출력
numbers = input('숫자를 입력해주세요.')
print(numbers)

try:
    if int(numbers) == 5:
        print('오오~')
    else:
        print('다른 숫자임')
except:
    print('숫자를 입력하지 않았음')