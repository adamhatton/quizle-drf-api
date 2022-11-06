from django.db import models
from django.contrib.auth.models import User
from quizzes.models import Quiz


class Score(models.Model):
    '''
    Score model (to hold fastest times)
    'owner' is a User instance, 'quiz' is a Quiz instance
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, related_name='scores', on_delete=models.CASCADE
    )
    completed_time = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        '''
        Orders Score objects in reverse order of when they were created.
        'unique_together' ensures a User can only have 1 score per quiz
        '''
        ordering = ['-created_on']
        unique_together = ['owner', 'quiz']

    def __str__(self):
        '''Returns the string representation of a model instance'''
        return f"{self.owner}'s score for {self.quiz.title}"
