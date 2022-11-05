from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    '''
    Quiz model
    '''
    category_choices = [
        ('', 'Pick a Category'),
        ('sport', 'Sport'),
        ('music', 'Music'),
        ('entertainment', 'Entertainment'),
        ('general', 'General Knowledge'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=13, choices=category_choices)
    time_limit_seconds = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    ans_1 = models.CharField(max_length=50)
    ans_2 = models.CharField(max_length=50)
    ans_3 = models.CharField(max_length=50)
    ans_4 = models.CharField(max_length=50)
    ans_5 = models.CharField(max_length=50)
    ans_6 = models.CharField(max_length=50)
    ans_7 = models.CharField(max_length=50)
    ans_8 = models.CharField(max_length=50)
    ans_9 = models.CharField(max_length=50)
    ans_10 = models.CharField(max_length=50)
    hint_1 = models.CharField(max_length=50)
    hint_2 = models.CharField(max_length=50)
    hint_3 = models.CharField(max_length=50)
    hint_4 = models.CharField(max_length=50)
    hint_5 = models.CharField(max_length=50)
    hint_6 = models.CharField(max_length=50)
    hint_7 = models.CharField(max_length=50)
    hint_8 = models.CharField(max_length=50)
    hint_9 = models.CharField(max_length=50)
    hint_10 = models.CharField(max_length=50)


    class Meta:
        '''
        Orders Quiz objects in reverse order of when they were created
        '''
        ordering = ['-created_on']

    def __str__(self):
        '''Returns the string representation of a model instance'''
        return f"{self.id} {self.title}"
