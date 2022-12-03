import requests
from pprint import pprint


def credits(title):
    # 1. search/movie에서 title검색을 통해서 movie_id를 받아온다.
    BASE_URL = 'https://api.themoviedb.org/3'
    #주소 뒷부분 상세 경로
    path = f'/search/movie'
    
    query_string = {
        'api_key': 'd77a958e646191ffe9107d07477129e7',
        'query' : title,
    }
    #reponse는 딕셔너리, 보통은 딕셔너리
    response = requests.get(BASE_URL + path, params = query_string).json()
    #pprint(response)
    #result는 리스트(api마다 응답이 다르게 오는데, 여기서는 리스트)
    result = response.get('results')
    if not result:
        return None
    else:
        movie_id = result[0].get('id')
    #pprint(movie_id)
    #id값으로 추천 영화 목록 가져온다.
    BASE_URL = 'https://api.themoviedb.org/3'
    #주소 뒷부분 상세 경로
    path = f'/movie/{movie_id}/credits'
    
    query_string = {
        'api_key': 'd77a958e646191ffe9107d07477129e7',
        'movie_id' : movie_id,
        'language': 'ko',
    }
    #reponse는 딕셔너리, 보통은 딕셔너리
    response = requests.get(BASE_URL + path, params = query_string).json()
    #pprint(response)
    #result는 리스트(api마다 응답이 다르게 오는데, 여기서는 리스트)
    result_cast = response.get('cast')
    result_crew = response.get('crew')
    ans = dict()
    cast = []
    crew = []
    if not result_cast:
        return None
    else:
        for i in range(len(result_cast)):
            if result_cast[i].get('cast_id') <10:
                cast.append(result_cast[i].get('name'))
        for j in range(len(result_crew)):
            if result_crew[j].get('department') == "Directing":
                crew.append(result_crew[j].get('name'))
        ans['cast'] = cast
        ans['crew'] = crew
        return ans


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
