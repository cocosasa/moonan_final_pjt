from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('reviews/', views.entire_review),
    path('movie/<int:movie_pk>/review/', views.create_review),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/comments/', views.create_review_comment),
    path('movie/reviews/<int:movie_pk>/', views.review_comment_of_the_movie),
    path('reviewcomments/<int:comment_pk>/', views.review_comment_detail),
    path('reviewcomments/<int:comment_pk>/comments/', views.review_ccomment_create),

    path('questions/', views.entire_questions),
    path('questions/create/', views.create_question),
    path('questions/<int:question_pk>/', views.question_detail),
    path('questions/<int:question_pk>/comments/', views.create_question_comment),
    path('questioncomments/<int:comment_pk>/', views.question_comment_detail),
    path('questioncomments/<int:comment_pk>/comments/', views.question_ccomment_create),
    path('quiz/correct/<int:points_get>/', views.choose_answer),
    path('questions/correct/<int:question_pk>/<int:comment_pk>/', views.select_comment),
]
