from django.contrib import admin
from .models import userinfo

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['id','name','sub','email','dob','address']

admin.site.register(userinfo,userAdmin)
