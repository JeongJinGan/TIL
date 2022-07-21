from urllib import response
import requests

URL = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=1&pageSize=20'

response = requests.get(URL).json()
# 삼성전자 주식
print(response.get('stocks')[0].get('closePrice'))
#print(response)