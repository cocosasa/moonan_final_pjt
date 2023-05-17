from rest_framework import serializers
from .models import Movie, Comment, Actor


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'vote_avg')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many = True, read_only = True)

    class Meta:
        model = Movie
        fields = '__all__'