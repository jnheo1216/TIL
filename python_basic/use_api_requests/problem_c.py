import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    api_key = 'b4893f302d08c4a823cdf51e8fcee9cc'
    maker = URLMaker(api_key)
    url = maker.get_url(region='KR', language='ko')
    res = requests.get(url)
    movie_dict = res.json()
    movie_list = movie_dict.get('results')

    # result = []
    # for movie in movie_list:
    #     result.append((movie.get('title'), movie.get('vote_average')))
    # result.sort(key=lambda x:x[1], reverse=True)
    ## 나는 영화 이름만 리턴하면 되는줄 알고 이렇게 할뻔

    movie_list.sort(key=lambda x:x['vote_average'], reverse=True)  # 리스트의 평점으로 정렬하는 lambda

    return movie_list[0:5]  # 상위 5개만 반환


if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())