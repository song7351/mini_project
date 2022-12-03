from rest_framework import serializers
from ..models import Review, Movie


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
