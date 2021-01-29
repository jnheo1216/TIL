import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    api_key = 'b4893f302d08c4a823cdf51e8fcee9cc'
    maker = URLMaker(api_key)
    url = maker.get_url(region='KR', language='ko')
    res = requests.get(url)
    movie_dict = res.json()
    movie_list = movie_dict.get('results')

    result = []
    for movie in movie_list:
        if movie.get('vote_average') > 8.0:  # 영화들 중에서 평점이 8점 이상인 것만
            result.append(movie)  # 결과에 추가
    
    return result


if __name__ == '__main__':
    pprint(vote_average_movies())    
