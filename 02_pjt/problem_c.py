from operator import itemgetter
import requests
from pprint import pprint


def ranking():
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
    sort_result = sorted(result, key=itemgetter('vote_average'))
    ans = []
    for i in range(-1, -6, -1):
      ans.append(sort_result[i])
    return ans

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
