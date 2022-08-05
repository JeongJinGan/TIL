import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL).json()
coins = response.get('data')

print(coins.get('prev_closing_price')) # 전일 BTC KRW의 종가


