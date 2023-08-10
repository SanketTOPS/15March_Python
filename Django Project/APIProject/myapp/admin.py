from django.contrib import admin
from .models import studInfo

# Register your models here.
class studData(admin.ModelAdmin):
    list_display=['name','sub','email']

admin.site.register(studInfo,studData)
