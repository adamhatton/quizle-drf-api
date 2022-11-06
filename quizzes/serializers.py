from rest_framework import serializers
from scores.models import Score
from likes.models import Like
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    ''' Serializer for Quiz model data '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    score_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    completed_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        '''
        Returns true if requested object is owned by the user
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        '''
        Returns the like.id if the quiz has been liked by the user
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, quiz=obj
            ).first()
            return like.id if like else None
        return None

    def get_score_id(self, obj):
        '''
        Returns the score.id if the user has completed the quiz
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            score = Score.objects.filter(
                owner=user, quiz=obj
            ).first()
            return score.id if score else None
        return None

    def validate_time_limit_seconds(self, value):
        '''
        Validates that time limit entered is in range of 0.5-10 minutes
        '''
        if value < 30 or value > 600:
            raise serializers.ValidationError(
                'Time limit must be between 30 seconds and 10 minutes'
            )
        return value

    def validate_category(self, value):
        '''
        Validates that a category has been selected
        '''
        if value == '':
            raise serializers.ValidationError(
                'Please select a category'
            )
        return value

    class Meta:
        ''' Metadata for Quiz Serializer '''
        model = Quiz
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'category',
            'time_limit_seconds',
            'created_on',
            'updated_on',
            'ans_1',
            'ans_2',
            'ans_3',
            'ans_4',
            'ans_5',
            'ans_6',
            'ans_7',
            'ans_8',
            'ans_9',
            'ans_10',
            'hint_1',
            'hint_2',
            'hint_3',
            'hint_4',
            'hint_5',
            'hint_6',
            'hint_7',
            'hint_8',
            'hint_9',
            'hint_10',
            'is_owner',
            'profile_id',
            'profile_image',
            'like_id',
            'score_id',
            'likes_count',
            'completed_count',
        ]
