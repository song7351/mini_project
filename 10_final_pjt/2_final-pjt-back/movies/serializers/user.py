from rest_framework import serializers
# 정확히는 settings에 accounts.User을 설정했기 때문에!
# FM은 accounts에 serializers/user.py가 맞음
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', )