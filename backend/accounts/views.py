from .models import Profile
from rest_framework import status
from .serializers import ProfileSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create_profile(request): 
    serializer = ProfileSerializer(data = request.data)

    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def profile(request, profile_pk) :
    profile = get_object_or_404(Profile, pk = profile_pk)
    
    if request.method == 'GET' :
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user == profile.user:
            serializer = ProfileSerializer(profile, data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response(serializer.data)
        return Response(status = status.HTTP_401_UNAUTHORIZED)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk = user_pk)
        if me != you:
            if you.followers.filter(pk = me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True

            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }

            return JsonResponse(context)
