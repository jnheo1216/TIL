import json
from pprint import pprint


# json 형태의 데이터를 가져와서 필요한 요소만으로 
# 다시 dictionary를 구성하여 반환하는 함수


def movie_info(movie):
    result_dict = {}
    result_dict['id'] = movie.get('id')
    result_dict['title'] = movie.get('title')
    result_dict['poster_path'] = movie.get('poster_path')
    result_dict['vote_average'] = movie.get('vote_average')
    result_dict['overview'] = movie.get('overview')
    result_dict['genre_ids'] = movie.get('genre_ids')

    return result_dict    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))