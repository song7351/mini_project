import requests
from pprint import pprint


def recommendation(title):
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
    path = f'/movie/{movie_id}/recommendations'
    
    query_string = {
        'api_key': 'd77a958e646191ffe9107d07477129e7',
        'movie_id' : movie_id,
        'language': 'ko',
    }
    #reponse는 딕셔너리, 보통은 딕셔너리
    response = requests.get(BASE_URL + path, params = query_string).json()
    #pprint(response)
    #result는 리스트(api마다 응답이 다르게 오는데, 여기서는 리스트)
    result = response.get('results')
    ans = []
    if not result:
        return []
    else:
        for i in range(len(result)):
            ans.append(result[i].get('title'))
        return ans

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
