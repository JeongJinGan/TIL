from urllib import response
import requests

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key' : '385e790f9c3c5a53d55c8b036acb92b4',
    'language' : 'ko-KR'
}

def popular_count():
    pass 
    # 여기에 코드를 작성합니다. 
    # get() 메소드를 통해 URL주소를 받아온다.
    # 받아온 URL로, 데이터를 요청하고 응답값을 받아옴.
    # 받아온 데이터를 딕셔너리로 변환한다. json()
    response = requests.get(BASE_URL+path, params=params).json() 
    # print(response) 영화 목록 출력 확인
    # print(len(response['results'])) 영화 목록의 개수 출력 확인
    # print(movie_dict['page']) 20 확인
    return (len(response['results']))
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
