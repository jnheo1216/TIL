import json
from pprint import pprint


# a에다가 추가로 genre라는 dict에서 genre_id를 
# genre_name으로 가져와서 반환내용에 포함함


def movie_info(movie, genres):
    result_dict = {}
    result_dict['id'] = movie.get('id')
    result_dict['title'] = movie.get('title')
    result_dict['poster_path'] = movie.get('poster_path')
    result_dict['vote_average'] = movie.get('vote_average')
    result_dict['overview'] = movie.get('overview')

    genre_dict = {}
    for genre in genres:
        genre_dict[genre['id']] = genre.get('name')

    genre_names = []
    for i in movie.get('genre_ids'):
        if int(i) in genre_dict:
            genre_names.append(genre_dict[i])
    
    result_dict['genre_names'] = genre_names

    return result_dict

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))