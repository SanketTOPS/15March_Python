from django.db import models

# Create your models here.

class studInfo(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    sub=models.CharField(max_length=20)
    email=models.EmailField()
    