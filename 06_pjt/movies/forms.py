from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description',)
        # all의 경우 유저를 선택할 수 있게됨. 그러나 게시글 작성은
        # 현재 로그인 사용자가 무조건 작성자가 되어야 함.
        # fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # movie와 user를 제외하는 이유
        # -> 댓글은 게시글에 속하고 로그인 사용자가 작성하기 때문
        exclude = ('movie', 'user',)
