from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Genre, Actor, Recommended
from accounts.models import Profile
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer, ActorSerializer, RecommendedSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
# filter 메서드에 or, and, not 등 다양한 조건을 줄 수 있게 하는 모듈
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
import random



@api_view(['GET'])
def entire_movies(request):
    movies = list(get_list_or_404(Movie))
    movies.sort(key = lambda x : x.popularity, reverse = True)
    serializers = MovieListSerializer(movies, many = True)
    return Response(serializers.data)



@api_view(['GET'])
def movies_with_genre(request, selected_genres, sortby):

    selected_movies = []

    for genre in selected_genres.split():
        movies = Movie.objects.filter(Q(genres__name__icontains = genre))

        for movie in list(movies):
            if movie not in selected_movies:
                selected_movies.append(movie)

    if sortby == 1:
        selected_movies.sort(key = lambda x : x.popularity, reverse = True)

    else:
        selected_movies.sort(key = lambda x : x.vote_avg, reverse = True)

    serializer = MovieListSerializer(selected_movies, many = True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)


@api_view(['GET'])
def entire_genres(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_search(request, search):
    for word in search.split():
        movies = Movie.objects.filter(Q(title__icontains = word) | Q(overview__icontains = word) | Q(genres__name__icontains = word))
        searched_movies = []
        for movie in list(movies):
                if movie not in searched_movies:
                    searched_movies.append(movie)
    searched_movies.sort(key = lambda x : x.popularity, reverse = True)
    serializer = MovieListSerializer(searched_movies, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def entire_movies_sorted_by_vote_avg(request):
    movies = list(get_list_or_404(Movie))
    movies.sort(key = lambda x : x.vote_avg, reverse = True)
    serializers = MovieListSerializer(movies, many = True)
    return Response(serializers.data)


@api_view(['GET'])
def entire_actors(request):
    actors = get_list_or_404(Actor)
    serializer = ActorSerializer(actors, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk = actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def recommend_movie(request):
    movielists = get_list_or_404(Recommended)
    serializer = RecommendedSerializer(movielists, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def recommend_user_movie(request):
#     user = request.user
#     profile = get_object_or_404(Profile, pk=user.id)
#     user_movies = []
#     user_movies.extend(profile.want_to_see_movies)
#     user_movies.extend(profile.watched_movies)
#     movies = get_list_or_404(Movie)
#     recommended_movies = movies.sort(key=lambda x: x.popularity, reverse=True)
#     print(recommend_movie)
#     recommended_movies = recommended_movies[:30]
#     recommended_movies = random.sample(recommended_movies, 12)
#     serializer = MovieListSerializer(recommended_movies, many=True)
#     return Response(serializer.data)

