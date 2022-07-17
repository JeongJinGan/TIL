import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    ids = movie['genre_ids']
    ids_name = []
    for genre in genres:
        if genre['id'] in ids:
            ids_name.append(genre['name']) 
    list = ['id','title','poster_path','vote_average','overview']
    dic = {}
    for key in list:
        dic[key] = movie[key]
    dic['gerne_names'] = ids_name
    return dic
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))