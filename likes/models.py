from django.db import models
from django.contrib.auth.models import User
from quizzes.models import Quiz


class Like(models.Model):
    '''
    Like model related to owner and quiz
    'owner' is a User instance, 'quiz' is a Quiz instance
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'quiz']

    def __str__(self):
        return f'{self.owner} {self.quiz}'