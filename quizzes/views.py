from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from quizle.permissions import IsOwnerOrReadOnly
from .models import Quiz
from .serializers import QuizSerializer


class QuizList(generics.ListCreateAPIView):
    '''
    List all quizzes and enable quiz creation
    '''
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Quiz.objects.annotate(
        likes_count=Count('likes', distinct=True),
        completed_count=Count('scores', distinct=True)
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = [
        'likes_count',
        'completed_count',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    filterset_fields = [
        'category',
        'owner',
        'scores__owner',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Display a single quiz and allow the owner to edit or delete it
    '''
    serializer_class = QuizSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Quiz.objects.annotate(
        likes_count=Count('likes', distinct=True),
        completed_count=Count('scores', distinct=True)
    ).order_by('-created_on')
