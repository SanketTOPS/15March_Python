from django.db import models
import datetime

# Create your models here.
class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True,blank=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    