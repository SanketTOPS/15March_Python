from django.shortcuts import render
from .forms import signupForm

# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')