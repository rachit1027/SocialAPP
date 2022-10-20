from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from user.models import Profile

# Create your views here.

def signup_view(request):
    '''Function to create a new user'''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        checkUser = Profile.objects.filter(user = username)
        if checkUser:
            messages.error(request,"User already exists")
            return redirect("/")
    
        if password == confirmpassword:
            user = User.objects.create_user(first_name=username,username=username,email=email,password=password)
            messages.success(request,f"User{username}created")
            user.save()
        else:
            messages.error(request,"Invalid credentials")
            #return render(request,'account/login.html')

    return render(request,'account/signup.html')


def login_view(request):
    '''Function to log in user'''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:# agar user ne kuch value di to login hoega
            login(request,user)
            messages.success(request,"Sucessfully LoggedIN")
            return redirect("home_page")
        else:#or agar nahi di to
            messages.error(request,"Invalid Credentials")
            return HttpResponse("Invalid Credentials")
    return HttpResponse("GET request")


def logout_view(request):
    logout(request)
    messages.success(request,"User loggedout")
    return redirect("/")