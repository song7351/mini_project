# requests 사용 예시 1

import requests

#응답을 요청시키는 주소
URL = 'https://dog.ceo/api/breeds/image/random'

#requests: 요청, get:전송방식
response = requests.get(URL).json()

#요청방식
'''
1. get
데이터 조회 = 주소창에 데이터를 넣는 방식
ex) 쿠팡 오징어 검색: www.cupang.com/q='오징어'
2. post
데이터 변경 -> DB데이터를 저장하는 공간(영향이 있는 경우)
주소창에는 표시가 안남
ex) 로그인: id와 password를 입력해도 db에 영향을 끼치고 보안이 필요한 데이터의 경우
post사용

'''
print(response)

#여기서 get은 딕셔너리의 get이다
'''
왜냐? 우리가 응답받은 결과는 json파일의 딕셔너리 형태로 전송받기 때문.
'''
results = response.get('message')
print(results)
