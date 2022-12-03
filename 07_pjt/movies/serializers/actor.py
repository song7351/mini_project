from rest_framework import serializers
from ..models import Actor, Movie

# serializer : 쿼리문으로 구성된 데이터를 JSON 포맷으로 쉽게 변환하게 해주는 객체
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
                            # many는 단일데이터가 아닐경우, read_only는 수정불가능
    movies = MovieSerializer(many = True, read_only = True)

    class Meta:
        model = Actor
        fields = '__all__'