from django.contrib import admin
from .models import userdata

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','mobile']

admin.site.register(userdata,userAdmin)