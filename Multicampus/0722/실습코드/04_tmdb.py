# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

import requests

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/76341'
params = {
    'api_key' : '<<api_key>>',
    'language' : 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)


