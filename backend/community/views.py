from movies.models import Movie
from accounts.models import Profile
from rest_framework import status
from rest_framework.response import Response
from .models import Review, ReviewComment, Question, QuestionComment
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from .serializers import ReviewSerializer, ReviewCommentSerializer, QuestionSerializer, QuestionCommentSerializer
from accounts.serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def entire_review(request):
    reviews = get_list_or_404(Review)
    serializers = ReviewSerializer(reviews, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = ReviewSerializer(data = request.data)
    
    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user, movie_id = movie)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print(review.user)
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review_comment(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    serializer = ReviewCommentSerializer(data = request.data)

    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user, review = review)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_comment_detail(request, comment_pk):
    comment = get_object_or_404(ReviewComment, pk = comment_pk)

    if request.method == 'GET':
        serializer = ReviewCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if comment.user == request.user:
            comment.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'PUT':
        if comment.user == request.user:
            serializer = ReviewCommentSerializer(comment, data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response(serializer.data)
        return Response(status = status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def review_comment_of_the_movie(request, movie_pk):
    reviews = get_list_or_404(Review, movie_id = movie_pk)
    serializers = ReviewSerializer(reviews, many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_ccomment_create(request, comment_pk):
    comment = get_object_or_404(ReviewComment, pk = comment_pk)
    serializer = ReviewCommentSerializer(data = request.data)

    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user, parent_comment = comment)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET'])
def entire_questions(request):
    questions = list(get_list_or_404(Question))
    serializers = QuestionSerializer(questions, many = True)
    return Response(serializers.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create_question(request):
    serializer = QuestionSerializer(data = request.data)
    
    me = get_object_or_404(Profile, user = request.user)

    if me.points < int(serializer.initial_data['points']):
        return Response(status = status.HTTP_400_BAD_REQUEST)

    serializer2 = ProfileSerializer(me, data=request.data)
    
    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user)

        if serializer2.is_valid(raise_exception = True):
            serializer2.save(points = me.points - serializer.data['points'])

            return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, question_pk):
    question = get_object_or_404(Question, pk = question_pk)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if question.user == request.user:
            serializer = QuestionSerializer(question, data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response(serializer.data)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'DELETE':
        if question.user == request.user:
            question.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question_comment(request, question_pk):
    question = get_object_or_404(Question, pk = question_pk)
    serializer = QuestionCommentSerializer(data = request.data)

    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user, question = question)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def question_comment_detail(request, comment_pk):
    comment = get_object_or_404(QuestionComment, pk = comment_pk)

    if request.method == 'GET':
        serializer = QuestionCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if comment.user == request.user:
            comment.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'PUT':
        if comment.user == request.user:
            serializer = QuestionCommentSerializer(comment, data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response(serializer.data)
        return Response(status = status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def question_ccomment_create(request, comment_pk):
    comment = get_object_or_404(QuestionComment, pk = comment_pk)
    serializer = QuestionCommentSerializer(data = request.data)

    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user, parent_comment = comment)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def choose_answer(request, points_get):
    me = get_object_or_404(Profile, user = request.user)
    serializer = ProfileSerializer(me, data = request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save(points = me.points + points_get)
        return Response(status = status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def select_comment(request, question_pk, comment_pk):
    question = get_object_or_404(Question, pk = question_pk)
    if question.is_completed == False:
        if request.user == question.user:
            comment = get_object_or_404(QuestionComment, pk = comment_pk)
            answerer = get_object_or_404(Profile, user = comment.user)
            serializer = ProfileSerializer(answerer, data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save(points = answerer.points + question.points)
                
                serializer2 = QuestionSerializer(question, data = request.data, partial = True)
                if serializer2.is_valid(raise_exception = True):
                    serializer2.save(is_completed = True)

                    serializer3 = QuestionCommentSerializer(comment, data = request.data, partial = True)
                    if serializer3.is_valid(raise_exception = True):
                        serializer3.save(is_chosen = True)
                return Response(status = status.HTTP_200_OK)
    return Response(status = status.HTTP_401_UNAUTHORIZED)