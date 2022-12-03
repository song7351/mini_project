import json
from pprint import pprint

#함수 재사용!!!!
#b번 문제: 장르값 불러오는 함수를 사용한다.
def genres_movie(movie, genres):
    genre_ids = movie.get('genre_ids')
    genre_names = []
    for i in range(len(genre_ids)):
        # genre_ids 순차 뽑기 = genre_ids[i]
        for j in range(len(genres)):
            if genres[j].get('id') == genre_ids[i]:
                genre_names.append(genres[j].get('name'))
    return genre_names    

def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    new_info = []
    for i in range(len(movies)):
        genre_ids = movies[i].get('genre_ids')
        genre_names = genres_movie( movies[i], genres)
        id = movies[i].get('id')
        overview = movies[i].get('overview')
        poster_path = movies[i].get('poster_path')
        title = movies[i].get('title')
        vote_average = movies[i].get('vote_average')
        info = {'genre_names':genre_names, 'id':id, 'overview':overview, 
                'poster_path':poster_path, 'title':title, 'vote_average':vote_average}    
        new_info.append(info)
    return new_info

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
