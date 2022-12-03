from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 20)   # 영화제목
    audience = models.IntegerField()            # 관객 수
    release_date = models.DateField()           # 개봉일
    genre = models.CharField(max_length=30)     # 장르
    score = models.FloatField()                 # 평점
    poster_url = models.TextField()             # 포스터 경로
    description = models.TextField()            # 줄거리

    def __str__(self):
        return self.title