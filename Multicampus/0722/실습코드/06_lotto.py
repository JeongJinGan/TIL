import requests

# 랜덤 하나 번호 고르고

# 실제로 내가 1024회동안 해당 번호로 샀으면 얼마를 벌었을까?
# 1 ~ 5등

for n in range(1, 10):
    URL = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
    response = requests.get(URL).json()
    print(response)