from django.shortcuts import render
from .forms import userForm
from .models import userdata

# Create your views here.

def index(request):
    if request.method=='POST':
        newdata=userForm(request.POST)
        if newdata.is_valid():
            newdata.save()
            print("Your data has been saved!")
        else:
            print(newdata.errors)
    return render(request,'index.html')

def showdata(request):
    data=userdata.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request):
    return render(request,'updatedata.html')