from django.contrib import admin
from django.urls import path
from noteapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('notes/',views.notes,name='notes'),
    path('userlogout/',views.userlogout),
]