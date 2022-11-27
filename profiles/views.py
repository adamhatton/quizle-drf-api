from django.db.models import Count
from rest_framework import generics
from quizle.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    '''
    List all profiles. Create is handled by user creation via signals
    '''
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        created_quizzes_count=Count('owner__quiz', distinct=True),
        completed_quizzes_count=Count('owner__score', distinct=True)
    ).order_by('-created_on')


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
    Displays a single profile and allows the owner to edit it
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        created_quizzes_count=Count('owner__quiz', distinct=True),
        completed_quizzes_count=Count('owner__score', distinct=True)
    ).order_by('-created_on')
