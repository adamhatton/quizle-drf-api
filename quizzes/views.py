from rest_framework import generics, permissions
from quizle.permissions import IsOwnerOrReadOnly
from .models import Quiz
from .serializers import QuizSerializer


class QuizList(generics.ListCreateAPIView):
    '''
    List all quizzes and enable quiz creation
    '''
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Quiz.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Displays a single quiz and allows the owner to edit or delete it
    '''
    serializer_class = QuizSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Quiz.objects.all()
