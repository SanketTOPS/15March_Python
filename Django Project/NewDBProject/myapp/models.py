from django.db import models

# Create your models here.

class userdata(models.Model):
    name=models.CharField(max_length=20)
    sub=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobile=models.BigIntegerField()