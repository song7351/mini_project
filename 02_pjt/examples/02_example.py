# requests 사용 예시 2

import requests


URL = 'https://api.agify.io'

params = {
    'name': 'michael',
    'country_id': 'KR',
}
'''
params는 파라미터라는 뜻으로
보통 한가지의 정보를 전달해서 요청할 경우에는 해당 정보만 변수만 전달하면되지만
여러가지 조건이 필요한 경우에는 params라는 딕셔너리를 만들어서 전달하면, 해당 key, value에 맞는걸 요청
'''
response = requests.get(URL, params=params).json()
print(response)
