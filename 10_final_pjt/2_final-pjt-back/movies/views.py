from .models import Movie, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers.movie import MovieListSerializer,MovieSerializer
from .serializers.review import ReviewSerializer
from .models import Movie, Review
import requests
import json

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        # articles = get_list_or_404(Article)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def review_create(reqeust, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=reqeust.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=reqeust.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
    # 좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
    # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
    # if request.user in article.like_users.all():
    
    # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인 
    if movie.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소 (remove)
        movie.like_users.remove(request.user)
    else:
        # 좋아요 추가 (add)
        movie.like_users.add(request.user)

    serializer = MovieSerializer(movie)
        # print(serializer.data)
    return Response(serializer.data)




@api_view(['POST'])
def review_likes(request, review_pk):
    if request.user.is_authenticated:
        review = Review.objects.get(pk=review_pk)
    # 좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
    # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
    # if request.user in article.like_users.all():
    
    # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인 
    if review.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소 (remove)
        review.like_users.remove(request.user)
    else:
        # 좋아요 추가 (add)
        review.like_users.add(request.user)

    serializer = ReviewSerializer(review)
        # print(serializer.data)
    return Response(serializer.data)
