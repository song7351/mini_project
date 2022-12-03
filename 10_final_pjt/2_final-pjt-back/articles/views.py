from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentListSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Article, Comment

# methods 허가
@api_view(['GET', 'POST'])
# 로그인 허가
# @permission_classes([IsAuthenticated])
def article_list(request):
    # 게시글 전체 조회
    if request.method == 'GET':
        # articles = get_list_or_404(Article)
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
        # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
                                # 자세한 에러정보제공
        if serializer.is_valid(raise_exception=True):
            # 작성자 정보 저장
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)

# 단일조회, 단일수정, 단일삭제
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # 요청자(=로그인유저) == 게시글작성자
        # 직접 한번 찍어보고 테스트 해보고 보세용
        # print(request.user)
        # print(article.user)
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            # 요청자가 권한이 없을경우
            data = {
                'update': False,
                'description': "로그인한 유저가 작성한 게시글이 아닙니다!"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            data = {
                'delete': f'article {article_pk} is deleted'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            data = {
                'delete': False,
                'description': "로그인한 유저가 작성한 게시글이 아닙니다!"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            data = {
                'update': False,
                'description': "로그인한 유저가 작성한 댓글이 아닙니다!"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            data = {
                'delete': f'comment {comment_pk} is deleted'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            data = {
                'delete': False,
                'description': "로그인한 유저가 작성한 댓글이 아닙니다!"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
