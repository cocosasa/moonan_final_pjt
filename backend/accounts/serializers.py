from .models import Profile, User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from movies.serializers import MovieListSerializer


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    followers_count = serializers.IntegerField(source = 'followers.count', read_only = True)
    followings = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    followings_count = serializers.IntegerField(source = 'followings.count', read_only = True)


    class Meta:
        model = get_user_model()
        fields = ('username', 'followers', 'followers_count', 'followings', 'followings_count')



class ProfileSerializer(serializers.ModelSerializer):

    want_to_see_movies = MovieListSerializer(many = True, required = False)
    watched_movies = MovieListSerializer(many = True, required = False)
    user = serializers.CharField(source = 'user.username', read_only = True)


    class Meta:
        model = Profile
        fields = '__all__'
