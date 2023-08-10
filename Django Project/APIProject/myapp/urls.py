from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('getdata/',views.getdata),
   path('getid/<int:id>/',views.getid),
]