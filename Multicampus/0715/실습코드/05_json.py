import json 
from pprint import pprint
# 파일을 열고, 

f = open('stocks.json', 'r', encoding='utf-8')
# JSON을 파이썬 객체 형식으로 한다!
kospi = json.load(f)
samsung = kospi['stocks'][0]
# print(samsung, type(samsung))

# stockName 정보랑, closePrice 정보만 가진 딕셔너리를 만들고 싶어요!
result = {
    'stockName': samsung.get('stockName'),
    'closePrice': samsung.get('closePrice')
}

print(result)