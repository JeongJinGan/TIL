import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '385e790f9c3c5a53d55c8b036acb92b4',
        'language' : 'ko-KR',
        'query' : title
    }

    response = requests.get(BASE_URL+path, params=params).json()
    movie_id = response.get('results')[0].get('id')
    
    result_dict = {'cast':[], 'crew':[]} 

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key' : '385e790f9c3c5a53d55c8b036acb92b4',
        'language' : 'ko-KR'
    }
    pass 
    # 여기에 코드를 작성합니다.  
    response2 = requests.get(BASE_URL+path, params=params).json()
    #print(response2.keys())

    if 'success' in response2.keys():
        return None

    for actor in response2['cast']:
        if actor['cast_id'] < 10:
            result_dict['cast'].append(actor['name'])

    for crew in response2['crew']:
        if crew['department'] == 'Directing':
            result_dict['crew'].append(crew['name']) 
    
    return result_dict               
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
