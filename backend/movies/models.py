from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 50)


class Actor(models.Model):
    name = models.CharField(max_length = 50)
    image = models.CharField(max_length = 200)


class Movie(models.Model):
    title = models.CharField(max_length = 100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length = 200)
    genres = models.ManyToManyField(Genre)
    # actors = models.ManyToManyField(Actor)


class Comment(models.Model):
    article = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.FloatField()
