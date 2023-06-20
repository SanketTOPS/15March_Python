from django.db import models

# Create your models here.

class userdata(models.Model):
    name=models.CharField(max_length=20)
    sub=models.CharField(max_length=20)
    dob=models.DateField()
    email=models.EmailField()
    mobile=models.BigIntegerField()
    address=models.TextField()