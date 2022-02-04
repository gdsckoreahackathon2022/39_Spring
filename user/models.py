from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=225)#불필요?
    birthyear = models.IntegerField()#불필요?
    gender = models.BooleanField()