import json

# 파일을 열고,
f = open('stocks.json','r',encoding='utf-8')
# JSON을 파이썬 객체 형식으로 한다.
kospi = json.load(f)
print(kospi['stocks'][0])