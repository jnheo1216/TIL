import json
import os
from pprint import pprint

# 날짜는 'release_date'에 있음 그거 슬라이싱해서 비교하는 함수


def dec_movies_with_os_module(movies):
    dec_movie_titles = []
    for i in os.listdir('data/movies'):
        movie_json = open(f'data/movies/{i}', encoding='UTF8')
        movie_list = json.load(movie_json)
        if int(movie_list.get('release_date')[5:-3]) == 12:
            dec_movie_titles.append(movie_list.get('title'))
            
    return dec_movie_titles

# d번과 마찬가지로 os안쓰는 것으로 만듬


def dec_movies(movies):
    
    dec_movie_titles = []
    id_lists = [movie.get('id') for movie in movies]

    for i in id_lists:
        movie_json = open(f'data/movies/{i}.json', encoding='UTF8')
        movie_list = json.load(movie_json)
        if int(movie_list.get('release_date')[5:-3]) == 12:
            dec_movie_titles.append(movie_list.get('title'))
            
    return dec_movie_titles
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))