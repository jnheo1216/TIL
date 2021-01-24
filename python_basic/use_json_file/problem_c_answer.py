import json
from pprint import pprint

# b와의 차이점은 들어오는 형식이 하나의 dict에서 여러개의 dict가 있는 list로 바뀐것 뿐


def movie_info(movies, genres):
    
    genre_dict = {}
    for genre in genres:
        genre_dict[genre['id']] = genre.get('name')
    
    result = []
    for movie in movies:
        result_dict = {}
        result_dict['id'] = movie.get('id')
        result_dict['title'] = movie.get('title')
        result_dict['poster_path'] = movie.get('poster_path')
        result_dict['vote_average'] = movie.get('vote_average')
        result_dict['overview'] = movie.get('overview')

        genre_names = []
        for i in movie.get('genre_ids'):
            if int(i) in genre_dict:
                genre_names.append(genre_dict[i])
        
        result_dict['genre_names'] = genre_names

        result.append(result_dict)

    return result
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))