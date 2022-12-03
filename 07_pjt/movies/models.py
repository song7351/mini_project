from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    # 배우와 영화는 다대다 관계
    # related_name='movies'는 역참조시 사용할 계획
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
