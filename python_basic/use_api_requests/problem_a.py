import requests
from tmdb import URLMaker


def popular_count():
    api_key = 'b4893f302d08c4a823cdf51e8fcee9cc'  # 키
    maker = URLMaker(api_key)  # 키를 생성자로 URLMaker객체 만듬
    url = maker.get_url(region='KR', language='ko')  # movie, popular로 url 받아옴
    # print(url)
    res = requests.get(url)  # 통신 ㄱㄱ
    movie_dict = res.json()  # 영화들 정보 받아옴
    movie_list = movie_dict.get('results')  # 영화들 리스트
    
    return len(movie_list)  # 영화 리스트 길이 반환


if __name__ == '__main__':
    print(popular_count())