from django.db import IntegrityError
from rest_framework import serializers
from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    ''' Serializer for Score model data '''
    owner = serializers.ReadOnlyField(source='owner.username')
    quiz_title = serializers.ReadOnlyField(source='quiz.title')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Returns true if requested object is owned by the user
        '''
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        ''' Metadata for Score Serializer '''
        model = Score
        fields = [
            'id',
            'owner',
            'quiz',
            'quiz_title',
            'completed_time',
            'created_on',
            'updated_on',
            'is_owner',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': (
                    'Error creating score. User already has a score for this quiz'
                )
            })
