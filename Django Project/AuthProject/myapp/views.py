from django.shortcuts import render, redirect
from .forms import signupForm
from .models import usersignup
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        user=usersignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login successful!")
            request.session['user']=unm # session create
            return redirect('home')
        else:
            print("Error!Login fail")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def home(request):
    data=request.session.get('user')
    return render(request,'home.html',{'data':data})

def userlogout(request):
    logout(request)
    return redirect('/')

def test(request):
    data=request.session.get('user')
    return render(request,'test.html',{'data':data})
