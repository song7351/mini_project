from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path("movies/", views.movie_list, name="movie_list"),
    path("movies/<int:movie_pk>/", views.movie_detail, name="movie_detail"),
    path('movies/<int:movie_pk>/likes/', views.likes, name='likes'),
    path("reviews/", views.review_list, name="review_list"),
    path("reviews/<int:review_pk>/", views.review_detail, name="review_detail"),
    path('reviews/<int:review_pk>/likes/', views.review_likes, name='review_likes'),
    path("movies/<int:movie_pk>/comments/", views.review_create, name="review_create"),
]
