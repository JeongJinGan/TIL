import requests

URL = 'https://api.agify.io'
params = {
    'name' : '정진'
}
response = requests.get(URL, params=params).json()
print(response)
