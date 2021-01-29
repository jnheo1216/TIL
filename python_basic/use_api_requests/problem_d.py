import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    api_key = 'b4893f302d08c4a823cdf51e8fcee9cc'
    maker = URLMaker(api_key)
    id_num = maker.movie_id(title)  # 함수다 입력받은 제목으로 movieid()를 통해 id 받음

    if not id_num:  # 영화가 없는 경우도 있음. 그럴떈 바로 None 반환
        return None

    recommendation_urlmaker = URLMaker(api_key)  # 받아온 영화아이디를 쓰기 위해 새롭게 객체 생성 
    recomendation_url = recommendation_urlmaker.get_url('movie', f'{id_num}/recommendations', region='KR', language='ko')
    # 영화추천은 movie/movie_id/recommendations 로 url이 이루어져있음. get_url에서 url받음

    response = requests.get(recomendation_url)  # 받은 url로 통신
    recomendation_movie_dict = response.json()  # 추천 영화 리스트를 받을 수 있다.

    result = []
    for movie_reco in recomendation_movie_dict.get('results'):  # 결과중에 제목만 따서 반환
        result.append(movie_reco.get('title'))
    
    return result


if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
