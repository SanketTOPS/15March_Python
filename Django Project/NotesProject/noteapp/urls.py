from django.contrib import admin
from django.urls import path,include
from noteapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('notes/',views.notes),
]