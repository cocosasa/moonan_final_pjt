from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('profile/', views.create_profile),
    path('profile/<str:username>/', views.profile),
    path('follow/<str:username>/', views.follow),
    path('watched/<int:movie_pk>/', views.watched),
    path('wanted/<int:movie_pk>/', views.wanted),
]