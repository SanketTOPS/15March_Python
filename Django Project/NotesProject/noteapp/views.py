from django.shortcuts import render,redirect
from .forms import signupForm,updateForm
from .models import userSignup
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            username=""
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get('username')
                try:
                    unm=userSignup.objects.get(username=username)
                    print("Username is already exists!")
                    messages.error(request,"Username is already exists!")
                except userSignup.DoesNotExist:
                    newuser.save()
                    print("Signup Successfully!")
                    messages.success(request,"Signup Successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            userid=userSignup.objects.get(username=unm)
            print("Current User:",userid.id)
            if user: #true
                print("Login Successfully!")
                messages.success(request,"Login Successfully!")
                request.session['user']=unm  #create a session
                request.session['userid']=userid.id  #create a session with userid
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
    userid=request.session.get('userid')
    cuser=userSignup.objects.get(id=userid)
    if request.method=='POST':
        update=updateForm(request.POST,instance=cuser)
        if update.is_valid():
            update.save()
            print("Profile Updated!")
        else:
            print(update.errors)
    return render(request,'profile.html',{'user':user,'userid':userSignup.objects.get(id=userid)})

def userlogout(request):
    logout(request)
    return redirect('/')