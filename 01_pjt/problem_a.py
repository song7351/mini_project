import json
from pprint import pprint


def movie_info(movie):
    genre_ids = movie.get('genre_ids')
    id = movie.get('id')
    overview = movie.get('overview')
    poster_path = movie.get('poster_path')
    title = movie.get('title')
    vote_average = movie.get('vote_average')
    info = {'genre_ids':genre_ids, 'id':id, 'overview':overview, 
            'poster_path':poster_path, 'title':title, 'vote_average':vote_average}
    return info

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
