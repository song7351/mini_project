0. 준비사항

```python
# server/
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata movies/fixtures/movies.json
python manage.py runserver

# client/
npm i
npm run serve
create: .env.local
```

1. 에러코드

```python
"""
에러코드: please commit your changes or stash them before you merge
해결방법
1. git stash 입력
2. git pull
3. 수정작업
4. add - commit - push
"""
```

2. 작업 일정
- 11월 16일
  
  - 기획서 작성 및 개발환경 준비

- 11월 17일
  
  - server
    
    - 영화, 리뷰, 영화찜, 리뷰좋아요 모델, 시리얼라이즈 구현
  
  - client
    
    - item을 제외한 전체 component 구성
    - server와 연결
    - 회원가입, 로그인까지 완료

- 11월 18일
  
  - server
    
    - db 자료 준비
  
  - client 
    
    - 영화자료 불러오기
    - 로그인, 로그아웃

- 11월 21일
  
  - client
    
    - 현재 상영중인 영화 api 작업
    
    - 계절 추천 영화자료 불러오기
    
    - 로그인, 로그아웃 유효성 검사작업
    
    - 전체 영화 페이지 css 및 pagination 작업
    
    - Home.vue 및 작업중인 vue css작업

- 11월 22일
  
  - client
    
    - 영화 상세페이지 작업
    
    - 리뷰 등록, 수정, 삭제 구현
    
    - 전체적인 css 작업 지속 진행

- 11월 23일
  
  - client
    
    - 영화 추천알고리즘 작업
    
    - 로그인 상태에 따른 상세설정 작업
    
    - 전체적인 css 작업 지속 진행

- 11월 24일
  
  - client
    
    - 영화 좋아요, 리뷰 좋아요 작업
    
    - 전체적인 css 작업 지속 진행

- 11월 25일
  
  - server
    
    - 게시판, 댓글 모델구현
    
    - 서버 배포
  
  - client
    
    - 게시판 vue 작업
    
    - 전체적인 css 작업 마무리
    
    - 서버 배포
