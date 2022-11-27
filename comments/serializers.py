from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    ''' Serializer for Comment Model data '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Returns true if requested object is owned by the user
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        '''
        Returns the humanized version of created_at
        '''
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        '''
        Returns the humanized version of updated_at
        '''
        return naturaltime(obj.updated_at)

    class Meta:
        ''' Metadata for Comment Serializer '''
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'quiz', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    '''
    Serializer for the Comment model used in Detail view
    '''
    quiz = serializers.ReadOnlyField(source='quiz.id')
