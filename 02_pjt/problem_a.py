import pprint
import requests


def popular_count():
    #우리가 최종 요청 주소:
    #https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=en-US&page=1
    #             보통 물음표 뒤가 params       ?api_key=<<api_key>>&language=en-US&page=1 
    #대문자 변수 = 상수
    BASE_URL = 'https://api.themoviedb.org/3'
    #주소 뒷부분 상세 경로
    path = '/movie/popular'
    
    #params: 요청할 데이터 조건들
    #같은 표현으로 query_string: 보통 ?뒤에 있기때문에
    query_string = {
        'api_key': 'd77a958e646191ffe9107d07477129e7',
        'language': 'ko',
        'region': 'KR',
    }
    #reponse는 딕셔너리, 보통은 딕셔너리
    response = requests.get(BASE_URL + path, params = query_string).json()
    #pprint.pprint(response)
    #result는 리스트(api마다 응답이 다르게 오는데, 여기서는 리스트)
    result = response.get('results')
    #pprint.pprint(result)
    return len(result)


if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    pprint.pprint(popular_count())
    # 20
