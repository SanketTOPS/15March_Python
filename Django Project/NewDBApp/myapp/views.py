from django.shortcuts import render
from .forms import userForm
from .models import userinfo

# Create your views here.

def index(request):
    if request.method=='POST':
        user=userForm(request.POST)
        if user.is_valid(): #true
            user.save()
            print("Your data has been saved!")
        else:
            print(user.errors)
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})