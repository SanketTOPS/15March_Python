from django.shortcuts import render,redirect
from .forms import userForm,updateForm
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

def updatedata(request,id):
    stid=userinfo.objects.get(id=id)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=stid)
            updateuser.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'stid':userinfo.objects.get(id=id)})


def deletedata(request,id):
    stid=userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect('showdata')

