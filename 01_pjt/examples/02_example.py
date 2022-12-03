# 데이터 추출 및 생성 예시

movie = {
    'genre_ids': [
        18,
        80
    ],
    'id': 278,
    'original_title': 'The Shawshank Redemption',
    'release_date': '1995-01-28',
    'title': '쇼생크 탈출',
    'vote_average': 8.7,
}

def make_dict(data):
    new_data = {
        '원제': data.get('original_title'),
        '개봉년도': data.get('release_date')[:4],
        '평점': data.get('vote_average')
    }
    return new_data

print(make_dict(movie))
