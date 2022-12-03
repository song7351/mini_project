from rest_framework import serializers
# 게시글에 댓글을 봐야하니깐
from ..models import Article, Comment
# 누가 썼는지 알아야 하니깐.
from .user import UserSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = ('id', 'user', 'content', 'created_at', 'updated_at')
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
