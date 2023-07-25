from django.db import models
from datetime import datetime

# Create your models here.
class userSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class mynotes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    query=models.CharField(max_length=100)
    option=models.CharField(max_length=100)
    files=models.FileField(upload_to='NotesFiles')
    comments=models.TextField()

class feedback(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    msg=models.TextField()

