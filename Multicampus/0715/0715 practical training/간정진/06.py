import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    dic = []
    for movie in movies:
        ids = movie['genre_ids'] 
        name = [] # ids(genre_ids)를 이름으로 변환한 값을 담을 리스트를 초기화.   
        for genre in genres:
            if genre['id'] in ids:
                name.append(genre['name'])
        
        list = ['id','title','poster_path','vote_average','overview']
        dict = {}

        for key in list:
            dict[key] = movie[key]
        dict['genre_names'] = name
        dic.append(dict)
    return dic
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))