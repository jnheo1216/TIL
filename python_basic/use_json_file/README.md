# pjt01

## prob_a

이건 문제 없이 해결. dict에 key와 value만 맞춰서 넣고 return하면 끝.



## prob_b

처음엔 좀 반복문이 많게 만들었다.

```python
# 장르 이름 찾아서 넣던 부분
    for i in movie.get('genre_ids'):
        for genre in genres:
            if genre['id'] == i:
                genre_names.append(genre['name'])
    result_dict['genre_names'] = genre_names
```

 'genre_ids'는 어처피 두어개라서 큰 루프는 아니지만, 

그리고 밑에 있을 problem_c 때문에 c에서 삼중반복문이 되는게 예쁘지 않음.

 ```python
    genre_dict = {}
    for genre in genres:
        genre_dict[genre['id']] = genre.get('name')
 ```

'genre_ids'에 있는 id 번호로 바로 검색하려고 dict만듬 .

```python
    genre_names = []
    for i in movie.get('genre_ids'):
        if int(i) in genre_dict:
            genre_names.append(genre_dict[i])    
    result_dict['genre_names'] = genre_names
```

다행히 줄임.



## prob_c

b랑 똑같다. 하나만 들어오던 것이 리스트로 들어옴.

```python
    result = []
    for movie in movies:
        '''
        .................방식은 b와 동일함...............
        '''
        result.append(result_dict)
```



## prob_d

movie폴더의 파일을 쉽게 가져오기 위해 `import os` 

```python
    for i in os.listdir('data/movies'):
        movie_json = open(f'data/movies/{i}', encoding='UTF8')
        movie_list = json.load(movie_json)
```

movie_list 안의 'buget'들을 비교하면 끝

근데 생각해보니 os쓰는 것은 아무래도 출제자의 의도가 아닌 것으로 보인다.

그래서 id리스트로 movie폴더의  json파일들을 여는 것으로 함수를 바꿈.

```python
id_lists = [movie.get('id') for movie in movies]
    for movie_id in id_lists:
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_list = json.load(movie_json)
```

prob_e도 그에 맞게 다시 바꿈.



## prob_e

prob_d와 같은 방식으로 movies안의 json파일들을 읽어옴.

개봉일은 json 파일 안에 'release_date'에 있다.

0000-XX-00의 형식으로 통일 되어 있으므로 `.get('release_date')[5:-3]` 으로 slicing해서 12와 비교.

맞으면 dec_movie_titles에 append하고 return 