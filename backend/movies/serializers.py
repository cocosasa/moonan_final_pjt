from rest_framework import serializers
from .models import Movie, Genre, Actor
from community.serializers import ReviewSerializer

class GenreSerializer(serializers.ModelSerializer):
    movie_genres = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    movie_genres_name = serializers.CharField(
        source='movie_genres.name', read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    starred_movies = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many = True, read_only = True)
    actors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(MovieListSerializer):
    movie_reviews = ReviewSerializer(many = True, read_only=True)
    actors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta(MovieListSerializer.Meta):
        fields = '__all__'


