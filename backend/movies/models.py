from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 50)


class Actor(models.Model):
    name = models.CharField(max_length = 100)
    image_path = models.CharField(max_length = 100, null = True)


class Movie(models.Model) :
    title = models.CharField(max_length = 50)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length = 300)
    genres = models.ManyToManyField(Genre, related_name = 'movie_genres')
    actors = models.ManyToManyField(Actor, related_name = 'starred_movies')