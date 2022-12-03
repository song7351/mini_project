from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie')
    title = models.CharField(max_length=100)    #영화제목
    movie_id = models.IntegerField() #영화 아이디
    youtube_id = models.CharField(max_length=100)   # 유튜브용 아이디
    overview = models.TextField()       # 줄거리
    release_date = models.DateField()   # 영화 개봉일
    vote_average = models.FloatField()  # 영화 평점 
    poster_path = models.CharField(max_length=200)  # 포스터 경로
    genres = models.ManyToManyField(Genre)  # 영화장르
    season = models.CharField(max_length=50)    # 영화계절태그

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review', blank=True)
    #  related_name
    #  reviews = ReviewSerializer(many=True, read_only=True)
    movie = models.ForeignKey("Movie", related_name="reviews", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    user_vote_average = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)