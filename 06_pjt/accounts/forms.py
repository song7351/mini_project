from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # get_user_model()을 사용해 Django에서 제공하는 유저 모델을 그대로 사용한다.
        # 단, 유저 셍성에서는 username과 email만 가져다 쓰겠다.
        model = get_user_model()
        fields = ('username', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

