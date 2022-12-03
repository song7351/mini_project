import json
from pprint import pprint
#배급한 영화가 많은 순으로 배급사 정렬하기
#

def movie_info(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    prod = {}
    for i in range(len(movies)):
        #폴더내 파일을 열기위한 파일이름(id)가 필요
        file_name = str(movies[i].get('id'))+'.json'
        #파일을 오픈하면 title과 revenue를 불러올 수 있다.
        json_movie = open(f'data/movies/{file_name}', encoding='utf-8')
        list_movie = json.load(json_movie)
        for j in range(len(list_movie.get("production_companies"))):
            name_prod = list_movie.get("production_companies")[j].get("name")
            if name_prod not in prod:
                prod[name_prod] = 1
            else:
                prod[name_prod] += 1
    cnt_prod = list(prod.values())
    erum_prod = list(prod.keys())
    for i in range(len(cnt_prod)-1):
        for j in range(i+1, len(cnt_prod)-1):
            if cnt_prod[i] < cnt_prod[j]:
                cnt_prod[i], cnt_prod[j] = cnt_prod[j], cnt_prod[i]
                erum_prod[i], erum_prod[j] = erum_prod[j], erum_prod[i]

    for i in range(len(erum_prod)):
        a = f"{i+1}순위 {erum_prod[i]}: {cnt_prod[i]}회"    
        print(a)

    return erum_prod

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    pprint(movie_info(movies_list))
