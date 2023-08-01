from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesForm,feedbackForm
from .models import userSignup
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from NotesProject import settings
import requests
import random

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
    if request.method=='POST':
        newfeedback=feedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your feedback has been saved successfully!")

            #Email Sending Code
            sub="Thank You!"
            msg=f"Dear User!\n\nThank you for your feedback, We will assist you.\n\nIf you have any query or doubt, Please contct on\nhelp@tops-int.com | +91 9724799469"
            from_ID=settings.EMAIL_HOST_USER
            #to_ID=['darshitgajjar2@gmail.com','aameta000@gmail.com','nihaltrivedi52@gmail.com','madhavivekariya777@gmail.com']
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)

            #OTP Sending 
            '''otp=random.randint(1111,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"KEGZf5czOn3eCxJPkWAFHQUYtS86Rbmrv1MyuViag4hs7N2DujvzKSw5MN9mRryb3LC4DsIHiWph78","variables_values":f"{otp}","route":"otp","numbers":"9825815881,8955973401,7016891480,7016475702"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)'''
        else:
            print(newfeedback.errors)
    return render(request,'contact.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
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