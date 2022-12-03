import json
from pprint import pprint


def movie_info(movie, genres):
    genre_ids = movie.get('genre_ids')
    genre_names = []
    for i in range(len(genre_ids)):
        # genre_ids 순차 뽑기 = genre_ids[i]
        for j in range(len(genres)):
            if genres[j].get('id') == genre_ids[i]:
                genre_names.append(genres[j].get('name'))
    id = movie.get('id')
    overview = movie.get('overview')
    poster_path = movie.get('poster_path')
    title = movie.get('title')
    vote_average = movie.get('vote_average')
    info = {'genre_names':genre_names, 'id':id, 'overview':overview, 
            'poster_path':poster_path, 'title':title, 'vote_average':vote_average}
    return info    

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
