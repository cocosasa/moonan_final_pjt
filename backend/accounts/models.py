from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'followers')



class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # nickname = models.CharField(max_length = 30, unique = True)
    points = models.IntegerField(default = 500)
    want_to_see_movies = models.ManyToManyField('movies.Movie', related_name = 'wants_users')
    watched_movies = models.ManyToManyField('movies.Movie', related_name = 'watches_users')
    profile_image = models.ImageField(null = True)