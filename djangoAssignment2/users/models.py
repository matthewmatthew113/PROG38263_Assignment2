#Import Django Various Django Libraries
from django.db import models
from django.contrib.auth.models import User

#Create your models here.

#Simple model text field for username in regards to user profiles, this field cannot be left blank.
class Profile(models.Model):
    username = models.TextField(User.username, blank=False)

    def __str__(self):
        return f'{self.user.username} Profile'