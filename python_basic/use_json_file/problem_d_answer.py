import json
import os

# movie폴더의 json 파일을 가져오기 위해 os.listdir로 하부 내용 가져옴


def max_revenue_with_os_module(movies):
    cost = 0
    get_title = ''
    for i in os.listdir('data/movies'):
        movie_json = open(f'data/movies/{i}', encoding='UTF8')
        movie_list = json.load(movie_json)
        if cost < movie_list.get('budget'):
            cost = movie_list.get('budget')
            get_title = movie_list.get('title')
    # print(cost, get_title)

    return get_title
        
# 근데 생각해보니 os 쓰는 것은 출제자의 의도가 아닌 것 같아서
# 안쓰는 것으로 함수 다시 만듬


def max_revenue(movies):
    cost = 0
    get_title = ''

    id_lists = [movie.get('id') for movie in movies]

    for movie_id in id_lists:
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_list = json.load(movie_json)
        if cost < movie_list.get('budget'):
            cost = movie_list.get('budget')
            get_title = movie_list.get('title')
    
    return get_title




 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))