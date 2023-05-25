from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.


class Review(models.Model):
    content = models.CharField(max_length=100)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'review_likers', null = True)
    movie_id = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name = 'movie_reviews')
    

class ReviewComment(models.Model):
    content = models.CharField(max_length = 100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    parent_comment = models.ForeignKey('self', on_delete = models.CASCADE, null = True, related_name = 'child_comments')
    review = models.ForeignKey(Review, on_delete = models.CASCADE, null = True, related_name = 'comments')


class Question(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    points = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    question_image = models.ImageField(blank = True)
    is_completed = models.BooleanField(default = False)
    

class QuestionComment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    parent_comment = models.ForeignKey('self', on_delete = models.CASCADE, null = True, related_name = 'child_comments')
    question = models.ForeignKey(Question, on_delete = models.CASCADE, null = True, related_name = 'question_comments')
    is_chosen = models.BooleanField(default = False)