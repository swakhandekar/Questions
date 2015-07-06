from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, default=0)
    title = models.CharField(max_length=500)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    ans = models.CharField(max_length=2)

    def __str__(self):
        return str(self.user)

class Student(models.Model):
    user = models.OneToOneField(User)
    count = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    temp = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)

class Votes(models.Model):
    ques = models.ForeignKey(Question)
    te = models.ForeignKey(User)

    def __str__(self):
        return str(self.te)
