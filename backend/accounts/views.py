from .models import Profile
from rest_framework import status
from .serializers import ProfileSerializer, UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from movies.models import Movie

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_profile(request): 
    serializer = ProfileSerializer(data = request.data)

    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def profile(request, username) :
    user = get_object_or_404(get_user_model(), username = username)
    profile = get_object_or_404(Profile, pk = user.id)
    
    if request.method == 'GET' :
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user == profile.user:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response(serializer.data)
        return Response(status = status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
        me = get_object_or_404(get_user_model(), username = username)
        you = request.user
        if me != you:
            if me.followers.filter(pk = you.pk).exists():
                me.followers.remove(you)
            else:
                me.followers.add(you)
            serializer = UserSerializer(me)
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def wanted(request, movie_pk):
    me = get_object_or_404(Profile, pk = request.user.pk)
    movie = get_object_or_404(Movie, pk = movie_pk)

    if me.want_to_see_movies.filter(pk = movie_pk).exists():
        me.want_to_see_movies.remove(movie)
        wanted = False
    else:
        me.want_to_see_movies.add(movie)
        wanted = True

        if me.watched_movies.filter(pk = movie_pk).exists():
            me.watched_movies.remove(movie)
            is_watched = False

    serializer = ProfileSerializer(me)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def watched(request, movie_pk):
    me = get_object_or_404(Profile, pk = request.user.pk)
    movie = get_object_or_404(Movie, pk = movie_pk)

    if me.watched_movies.filter(pk = movie_pk).exists():
        me.watched_movies.remove(movie)
        watched = False

    else:
        me.watched_movies.add(movie)
        watched = True

        if me.want_to_see_movies.filter(pk = movie_pk).exists():
            me.want_to_see_movies.remove(movie)
            wanted = False

    serializer = ProfileSerializer(me)
    return Response(serializer.data)
