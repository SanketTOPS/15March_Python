from django.shortcuts import render
from .forms import userForm

# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid(): #true
            newuser.save()
            print("your data has been submitted!")
        else:
            print(newuser.errors)
    return render(request,'index.html')