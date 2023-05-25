from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.entire_movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('genres/', views.entire_genres),
    path('search/movies/<str:search>/', views.movie_search),
    path('search/movies/genres/<str:selected_genres>/<int:sortby>/', views.movies_with_genre),
    path('vote_avg/', views.entire_movies_sorted_by_vote_avg),
    path('actors/', views.entire_actors),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('recommend/', views.recommend_movie),
    # path('recommend/user/', views.recommend_user_movie),

]