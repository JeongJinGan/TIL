import requests

order_currency = 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'


response = requests.get(URL).json()
coins = response.get('data')

# coins : 딕셔너리
# key : coin 이름
# value : 딕셔너리(코인의 정보)


for coin in coins:
    # coins.get(coin) <- 코인의 정보인 딕셔너리
    # 그 딕셔너리의 closing_price
    if coin != 'date':
        print(coin, coins.get(coin).get('closing_price'))
    










