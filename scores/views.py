from rest_framework import generics, permissions
from quizle.permissions import IsOwnerOrReadOnly
from .models import Score
from .serializers import ScoreSerializer


class ScoreList(generics.ListCreateAPIView):
    '''
    List all scores and enable score creation
    '''
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Score.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ScoreDetail(generics.RetrieveDestroyAPIView):
    '''
    Enable a single score to be retrieved and deleted
    '''
    serializer_class = ScoreSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Score.objects.all()
