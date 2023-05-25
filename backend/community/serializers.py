from rest_framework import serializers
from .models import Review, ReviewComment, Question, QuestionComment


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = 'user.username', read_only = True)
    comments = serializers.PrimaryKeyRelatedField(many = True, read_only = True, allow_null = True)

    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'created_at', 'updated_at', 'user', 'movie_id', 'comments',)
        read_only_fields = ('user', 'movie_id')


class ReviewCommentSerializer(serializers.ModelSerializer):
    child_comments = serializers.PrimaryKeyRelatedField(many = True, read_only = True, allow_null = True)

    class Meta:
        model = ReviewComment
        fields = ('id', 'review', 'content', 'user', 'created_at', 'updated_at', 'parent_comment', 'child_comments')
        read_only_fields = ('user', 'review', 'parent_comment')


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(
            instance, context=self.context)
        return serializer.data


class QuestionCommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = 'user.username', read_only = True)

    # child_comments = serializers.PrimaryKeyRelatedField(many = True, read_only = True, allow_null = True)
    child_comments = RecursiveSerializer(many=True, read_only=True)
    class Meta:
        model = QuestionComment
        fields = ('id', 'question', 'content', 'user', 'created_at', 'updated_at', 'parent_comment', 'child_comments', 'is_chosen',)
        read_only_fields = ('user', 'question', 'parent_comment')
    
    def get_reply(self, instance):
        # recursive
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = 'user.username', read_only = True)
    question_comments = QuestionCommentSerializer(many = True, read_only = True, allow_null = True)
    
    class Meta:
        model = Question
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'points', 'user', 'question_comments', 'question_image', 'is_completed')
        read_only_fields = ('user',)