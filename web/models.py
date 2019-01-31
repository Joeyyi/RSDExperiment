from django.db import models

# Create your models here.

class Subject(models.Model):
  name = models.CharField(max_length=20)
  date_created = models.DateTimeField('date created')
  age = models.IntegerField('age')

# class Survey(models.Model):

# https://blog.csdn.net/myhuashengmi/article/details/53106301