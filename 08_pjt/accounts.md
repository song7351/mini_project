### 1. model
```python
    from django.db import models 
    from django.contrib.auth.models import AbstractUser 
        
    class User(AbstractUser): 
        followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```
accounts_user 와 다른 accounts_user가 ManyToMany 관계로 엮여있는 상태이다.
또한 비대칭 상태(A유저가 B유저를 팔로우로 끝나는것)이므로 symetrical을 지정한다.

cf) 대칭상태 = A유저가 B유저를 팔로우하면 B유저도 A유저를 팔로우

### 2. views
```python
    @require_POST 
    def follow(request, user_pk): 
        if request.user.is_authenticated: 
            person = get_object_or_404(get_user_model(), pk=user_pk) 
            user = request.user 
            if person != user: 
                if person.followers.filter(pk=user.pk).exists(): 
                    person.followers.remove(user) 
                    followed = False 
                else: 
                    person.followers.add(user) 
                    followed = True 
                context = { 
                    'isFollowed': followed, 
                    'followers_count': person.followers.count(), 
                    'followings_count': person.followings.count(), 
                } 
                return JsonResponse(context) 
        return HttpResponse(status=401)
```
user_pk: 내(로그인 사용자)가 팔로우할 상대방 pk
person: 상대방 pk를 사용하여 user정보를 가져온다.
user: 나의 정보
person.followers: 우리는 User모델에서 다대다관계로 설정한 followings필드를 followers로 사용하기로 설정했다. 그래서 해당 필드에 접근해서 나의 정보(pk)가 있는지 확인하고 작업한다.
---
```python
    @login_required 
    def profile(request, username): 
        person = get_object_or_404(get_user_model(), username=username) 
        context = { 
            'person': person, 
        } 
        return render(request, 'accounts/profile.html', context)
```
내 profile만 볼 수 있는게 아니라 다른 사람의 profile도 볼 수 있어야 하므로
username이 일치한ㄴ지 확인해서 person 정보를 가져온다.
