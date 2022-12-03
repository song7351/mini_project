import json

def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    title_movie = []
    for i in range(len(movies)):
        #폴더내 파일을 열기위한 파일이름(id)가 필요
        file_name = str(movies[i].get('id'))+'.json'
        #파일을 오픈하면 title과 revenue를 불러올 수 있다.
        json_movie = open(f'data/movies/{file_name}', encoding='utf-8')
        list_movie = json.load(json_movie)
        month_movie = list_movie.get("release_date")[5:7]
        if month_movie == '12':
            title_movie.append(list_movie.get('title'))
        
    return title_movie
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
