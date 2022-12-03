from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 어드민 사이트에 커스텀유저 모델 등록
admin.site.register(User, UserAdmin)
