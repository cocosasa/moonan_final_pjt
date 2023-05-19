from rest_framework import serializers
from .models import Review, ReviewComment, Question, QuestionComment



class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'created_at', 'updated_at', 'user', 'like_users', 'movie_id')
        read_only_fields = ('user', 'movie_id')


class ReviewCommentSerializer(serializers.ModelSerializer):
    child_comments = serializers.PrimaryKeyRelatedField(many = True, read_only = True, allow_null = True)

    class Meta:
        model = ReviewComment
        fields = ('id', 'review', 'content', 'user', 'created_at', 'updated_at', 'parent_comment', 'child_comments')
        read_only_fields = ('user', 'review', 'parent_comment')


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'points', 'user')
        read_only_fields = ('user',)


class QuestionCommentSerializer(serializers.ModelSerializer):
    child_comments = serializers.PrimaryKeyRelatedField(many = True, read_only = True, allow_null = True)

    class Meta:
        model = QuestionComment
        fields = ('id', 'question', 'content', 'user', 'created_at', 'updated_at', 'parent_comment', 'child_comments')
        read_only_fields = ('user', 'question', 'parent_comment')