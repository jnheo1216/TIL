import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    api_key = 'b4893f302d08c4a823cdf51e8fcee9cc'
    maker = URLMaker(api_key)
    id_num = maker.movie_id(title)

    if not id_num:
        return None
    
    detail_urlmaker = URLMaker(api_key)  # 영화 출연배우, 연출진정보를 받는 url을 받기 위해 객체 생성
    detail_url = detail_urlmaker.get_url('movie', f'{id_num}/credits', region='KR', language='ko')
    # 영화 출연진에 대한 정보는 movie/movie_id/credits 에서 얻을 수 있다.

    response = requests.get(detail_url)
    movie_info = response.json()  # 영화 정보를 받아옴

    result_cast = []
    result_crew = []
    for i in movie_info.get('cast'):  # 영화배우의 경우
        if i.get('cast_id') < 10:  # cast_id가 10보다 작은 사람들만
            result_cast.append(i.get('name'))  # 추가해줌
    for j in movie_info.get('crew'):  # 영화 제작진의 경우
        if j.get('known_for_department') == 'Directing':  # 감독을
            result_crew.append(j.get('name'))  # 추가해줌
    
    result_crew = list(set(result_crew))  # 중복값 없애주기. (봉준호만 3번 나오길래)

    return {'cast': result_cast, 'crew': result_crew}


if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None