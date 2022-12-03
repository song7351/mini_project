import json

from problem_d import max_revenue
#90년대 개봉작 중 많은 수입을 올린 영화 순위

def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    title_movies = []
    revenue_movies = []
    for i in range(len(movies)):
        #폴더내 파일을 열기위한 파일이름(id)가 필요
        file_name = str(movies[i].get('id'))+'.json'
        #파일을 오픈하면 title과 revenue를 불러올 수 있다.
        json_movie = open(f'data/movies/{file_name}', encoding='utf-8')
        list_movie = json.load(json_movie)
        month_movie = list_movie.get("release_date")[:4]
        month_movie = int(month_movie)
        if 1989 < month_movie < 2000:
            title_movies.append(list_movie.get('title'))
            revenue_movies.append(list_movie.get('revenue'))
    for i in range(len(title_movies)):
        for j in range(i+1, len(title_movies)):
            if revenue_movies[i] < revenue_movies[j]:
                revenue_movies[i], revenue_movies[j] = revenue_movies[j], revenue_movies[i]
                title_movies[i], title_movies[j] = title_movies[j], title_movies[i]
        
    for i in range(len(title_movies)):
        a = f"{i+1}순위는 {title_movies[i]}입니다."    
        print(a)
    return title_movies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
