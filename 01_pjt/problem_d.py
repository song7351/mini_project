import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    # 수익이 최고일 경우
    max_rev = 0
    max_title = ''  
    for i in range(len(movies)):
        #폴더내 파일을 열기위한 파일이름(id)가 필요
        file_name = str(movies[i].get('id'))+'.json'
        #파일을 오픈하면 title과 revenue를 불러올 수 있다.
        json_movie = open(f'data/movies/{file_name}', encoding='utf-8')
        list_movie = json.load(json_movie)
        if list_movie.get('revenue') > max_rev:
            max_rev = list_movie.get('revenue')
            max_title = list_movie.get('title')
    
    return max_title
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
