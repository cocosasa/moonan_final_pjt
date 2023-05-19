from rest_framework import serializers
from .models import Movie, Genre


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(MovieListSerializer):
    
    class Meta(MovieListSerializer.Meta):
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    genre_movies = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta:
        model = Genre
        fields = '__all__'