# pjt02

## prob_a

popular를 기준으로 받아온 데이터를 토대로 영화 개수를 반환

```python
def popular_count():
    api_key = 'b4893f302d08c4a823cdf51e8fcee9cc'  # 키
    maker = URLMaker(api_key)  # 키를 생성자로 URLMaker객체 만듬
    url = maker.get_url(region='KR', language='ko')  # movie, popular로 url 받아옴
    # print(url)
    res = requests.get(url)  # 통신 ㄱㄱ
    movie_dict = res.json()  # 영화들 정보 받아옴
    movie_list = movie_dict.get('results')  # 영화들 리스트
    
    return len(movie_list)  # 영화 리스트 길이 반환
```

```
20
```

미리 tmdb에 가입하여 받은 키로 URLMaker객체를 만든다.

get_url 인스턴스로 완성된 url을 받는다.

request 모듈로 통신, 받은 정보의 길이를 return 



## prob_b

영화 리스트중에 평점 8점이 넘는 것들의 정보만 반환

```python
def vote_average_movies():
	'''
	받아오는 부분은 1번과 동일하므로 README에선 생략
	'''

    result = []
    for movie in movie_list:
        if movie.get('vote_average') > 8.0:  # 영화들 중에서 평점이 8점 이상인 것만
            result.append(movie)  # 결과에 추가
    
    return result
```

```
[{'adult': False,
  'backdrop_path': '/kf456ZqeC45XTvo6W9pW5clYKfQ.jpg',
  'genre_ids': [10751, 16, 35, 18, 10402, 14],
  'id': 508442,
  'original_language': 'en',
  'original_title': 'Soul',
  'overview': '뉴욕에서 음악 선생님으로 일하던 조는 꿈에 그리던 최고의 밴드와 재즈 클럽에서 연주하게 된 그 날, 예기치 못한 '
              '사고로 영혼이 되어 태어나기 전 세상에 떨어진다. 탄생 전 영혼들이 멘토와 함께 자신의 관심사를 발견하면 지구 '
              '통행증을 발급하는 태어나기 전 세상. 조는 그 곳에서 유일하게 지구에 가고 싶어하지 않는 시니컬한 영혼 22의 '
              '멘토가 된다. 링컨, 간디, 테레사 수녀도 멘토되길 포기한 영혼 22, 꿈의 무대에 서려면 22의 지구 통행증이 '
              '필요한 조. 그는 다시 지구로 돌아가 꿈의 무대에 설 수 있을까?',
  'popularity': 1971.071,
  'poster_path': '/qJiaB4RJMM5Oh6A4rqrEOHQUJbu.jpg',
  'release_date': '2021-01-20',
  'title': '소울',
  'video': False,
  'vote_average': 8.3,
  'vote_count': 4234},
 {'adult': False,
  'backdrop_path': '/n6bUvigpRFqSwmPp1m2YADdbRBc.jpg',
  'genre_ids': [80, 53, 18],
  'id': 475557,
  'original_language': 'en',
  'original_title': 'Joker',
  'overview': '홀어머니와 사는 아서 플렉은 코미디언을 꿈꾸지만 그의 삶은 좌절과 절망으로 가득 차 있다. 광대 아르바이트는 '
              '그에게 모욕을 가져다주기 일쑤고, 긴장하면 웃음을 통제할 수 없는 신경병 증세는 그를 더욱 고립시킨다. 정부 예산 '
              '긴축으로 인해 정신과 약물을 지원하던 공공의료 서비스마저 없어져 버린 어느 날, 아서는 지하철에서 시비를 걸어온 '
              '증권사 직원들에게 얻어맞던 와중에 동료가 건네준 권총으로 그들을 쏴 버리고 만다. 군중들은 지배계급에 대한 저항의 '
              '아이콘이 된 그를 추종하기 시작하며 광대 마스크로 얼굴을 가리고 거리로 쏟아져 나오기 시작하는데...',
  'popularity': 551.847,
  'poster_path': '/wrCwH6WOvXQvVuqcKNUrLDCDxdw.jpg',
  'release_date': '2019-10-02',
  'title': '조커',
  'video': False,
  'vote_average': 8.2,
  'vote_count': 16503}]
```

조커, 소울 두 영화만 8점이 넘는 것을 확인할 수 있음



## prob_c

받아온 영화의 리스트를 평점순으로 정렬해서 반환하는 함수

```python
def ranking():
	'''
	받아오는 부분은 1번과 동일하므로 README에선 생략
	'''

    # result = []
    # for movie in movie_list:
    #     result.append((movie.get('title'), movie.get('vote_average')))
    # result.sort(key=lambda x:x[1], reverse=True)
    ## 나는 영화 이름만 리턴하면 되는줄 알고 이렇게 할뻔

    movie_list.sort(key=lambda x:x['vote_average'], reverse=True)  # 리스트의 평점으로 정렬하는 lambda

    return movie_list[0:5]  # 상위 5개만 반환
```

```
## 원래는 정보 다 가져오는 거지만 생략해서 여기에는 이름과 평점만 씀 ##
## 위 코드 실행하면 다 가져옴 ##
[('소울', 8.3), ('조커', 8.2), ('익스트랙션', 7.4), ('테넷', 7.3), ('나쁜 녀석들: 포에버', 7.2)]
```

sort와 lambda로 리스트를 'vote_average'순으로 정렬함



## prob_d

영화 제목으로 영화id를 받아서 그걸로 연관추천영화 받아오는 함수

```python
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
```

```
['원스 어폰 어 타임 인… 할리우드',
 '조조 래빗',
 '결혼 이야기',
 '나이브스 아웃',
 '1917',
 '조커',
 '아이리시맨',
 '미드소마',
 '라이트하우스',
 '그린 북',
 '언컷 젬스',
 '어스',
 '더 플랫폼',
 '블랙클랜스맨',
 '포드 V 페라리',
 '더 페이버릿: 여왕의 여자',
 '두 교황',
 '작은 아씨들',
 '테넷',
 '브레이킹 배드 무비: 엘 카미노']
[]
None
```

그래비티는 연관 추천영화가 없어서 빈 리스트를 반환함

id없는영화는 movie_id 자체가 안되서 None값을 반환하는 걸 확인



## prob_e

배우들과 감독들의 정보를 가져와서 반환하는 함수

```python
def credits(title):
	'''
	id 받아오는 부분은 d번과 동일하므로 README에선 생략
	'''
    
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
```

```
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Chang Hyae-jin'],
 'crew': ['Bong Joon-ho',
          'Lee Jung-hoon',
          'Yoon Young-woo',
          'Park Hyun-cheol',
          'Kim Dae-hwan',
          'Kim Seong-sik']}
None
```

영화 출연진에 대한 정보는 movie/movie_id/credits 에서 얻음

영화배우는 cast_id가 10미만인 경우만 결과값에 추가, 영화제작진은 Directing만 추가.

반환할 crew에 중복값이 있어서 중복값을 지우기 위해  list(set(result_crew))를 함.