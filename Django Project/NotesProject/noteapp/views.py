from django.shortcuts import render,redirect
from .forms import signupForm
from .models import userSignup
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                messages.success(request,"Signup Successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                messages.success(request,"Login Successfully!")
                request.session['user']=unm  #create a session
                return redirect('notes')
            else:
                print("Error!Login faild....Try again")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    return render(request,'profile.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')