import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key' : '385e790f9c3c5a53d55c8b036acb92b4',
    'language' : 'ko-KR'
}

def ranking():
    pass 
    # 여기에 코드를 작성합니다.  
    response = requests.get(BASE_URL+path, params=params).json() 
    # 영화 데이터를 담고 있는 곳
    movie_results = response.get('results')
    # print(movie_results)

    # 정렬시 sorted 함수의 key를 활용 ==> Lambda
    movie_results_sort = sorted(movie_results, key = lambda x: x['vote_average'], reverse=True)
    # vote_average 8.4 ~ ... ~ 5.4
    # print(movie_results_sort)
    # vote_average 8.4 ~ ... ~ 7.9
    movie_results_sort_5 = movie_results_sort[:5]
    return movie_results_sort_5
    # movie_results_sort = sorted(movie_results)
    # movie_results_sort_5 = movie_results_sort[:5]
    # print(movie_results_sort_5)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
