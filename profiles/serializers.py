from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    ''' Serializer for Profile Model data '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_quizzes_count = serializers.ReadOnlyField()
    completed_quizzes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        '''
        Returns true if requested object is owned by the user
        '''
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        '''
        Validates that profile image is smaller than 2MB
        '''
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        return value

    class Meta:
        ''' Metadata for Profile Serializer '''
        model = Profile
        fields = [
            'id',
            'owner',
            'bio',
            'image',
            'name',
            'created_on',
            'updated_on',
            'is_owner',
            'created_quizzes_count',
            'completed_quizzes_count',
        ]
