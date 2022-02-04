from ast import mod
from venv import create
from django.db import models
from user.models import User


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=225)
    host = models.CharField(max_length=225)
    surveiee = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
