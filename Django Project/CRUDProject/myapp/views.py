from django.shortcuts import render,redirect
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

def updatedata(request,id):
    stid=userdata.objects.get(id=id)
    if request.method=='POST':
        updateuser=userForm(request.POST,instance=stid)
        if updateuser.is_valid():
            #updateuser=userForm(request.POST)
            updateuser.save()
            print("Update successfully!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=userdata.objects.get(id=id)
    userdata.delete(stid)
    return redirect('showdata')

    
