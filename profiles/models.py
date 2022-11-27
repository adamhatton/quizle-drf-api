from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Profile model.
    Extends user model with additional information about user
    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Default profile image taken from:
    # https://pixabay.com/vectors/user-icon-person-personal-about-me-2935527/
    image = models.ImageField(
        upload_to='images/', default='../default_user_geiijk'
    )
    name = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        '''
        Orders Profile objects in reverse order of when they were created
        '''
        ordering = ['-created_on']

    def __str__(self):
        '''Returns the string representation of a model instance'''
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    '''Creates a Profile object if a User has been created'''
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
