from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# auth.models.AbstractUser 를 상속받은 User 모델을 사용할 것이다. pass라고 되어 있지만,
# 실제로 상속된 내용 모두가 들어가며, 이것이 커스텀 유저 모델이 된다.