# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력
number = input()

try:
    print(100/int(number))
# 파이썬에서 제공하는 에러 + 내가 지정한 오류 메시지
except ZeroDivisionError as err:
    print('0으로는 나눌 수가 없습니다.')
except ValueError:
    print('숫자 형식으로 입력해주세요.')
except Exception:
    print('오류')