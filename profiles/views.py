from rest_framework import generics
from quizle.permissions import isOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    '''
    List all profiles. Create is handled by user creation via signals
    '''
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
