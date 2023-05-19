from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('movies/<int:movie_pk>/reviews/', views.create_review),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/comments/', views.create_review_comment),
    path('reviewcomments/<int:comment_pk>/', views.review_comment_detail),
    path('reviewcomments/<int:comment_pk>/comments/', views.review_ccomment_create),

    path('questions/', views.create_question),
    path('questions/<int:question_pk>/', views.question_detail),
    path('questions/<int:question_pk>/comments/', views.create_question_comment),
    path('questioncomments/<int:comment_pk>/', views.question_comment_detail),
    path('questioncomments/<int:comment_pk>/comments/', views.question_ccomment_create),
]
