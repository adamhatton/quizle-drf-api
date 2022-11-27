from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    ''' Serializer for Like model data '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        ''' Metadata for Score Serializer '''
        model = Like
        fields = ['id', 'owner', 'quiz', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Error creating like. User already liked this quiz'
            })
