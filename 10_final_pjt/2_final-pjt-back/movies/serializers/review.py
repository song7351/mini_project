from rest_framework import serializers
from ..models import Movie, Review
from .user import UserSerializer

# review
# class ReviewSerializer(serializers.ModelSerializer):
#     # username = serializers.CharField(source='user.username', read_only=True)
#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('movie',)


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', )
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        # fields = ('content', 'user_vote_average', 'created_at', 'user', 'movie','id')
        fields = '__all__'
