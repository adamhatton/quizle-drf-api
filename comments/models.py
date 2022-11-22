from django.db import models
from django.contrib.auth.models import User
from quizzes.models import Quiz


class Comment(models.Model):
    '''
    Comment model, related to User and Post
    'owner' is a User instance, 'quiz' is a Quiz instance
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content