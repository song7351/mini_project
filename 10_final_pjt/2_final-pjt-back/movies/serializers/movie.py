from rest_framework import serializers
from ..models import Movie, Review
from .user import UserSerializer
from .review import ReviewSerializer

# movie list
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'genres', 'season', 'like_users')


# movie detail 
class MovieSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)

        class Meta:
            model = Review
            fields = '__all__'
    reviews = ReviewSerializer(many=True, read_only=True)
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


