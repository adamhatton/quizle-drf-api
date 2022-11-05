from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    ''' Serializer for Profile Model data '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Returns true if requested object is owned by the user
        '''
        request = self.context['request']
        return request.user == obj.owner

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
            'updated_on'
            'is_owner',
        ]
        