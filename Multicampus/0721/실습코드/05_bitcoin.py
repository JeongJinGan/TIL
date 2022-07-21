from urllib import response
import requests

URL = 'https://api.bithumb.com/public/ticker/BTC_KRW'
response = requests.get(URL).json()
print(response)