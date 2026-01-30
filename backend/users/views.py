from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


# Mambo ya kulogin

def user_login(request):
    if request.methos=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request(username=username,password=password))
        if user is not None:
            login(user)
            messages.success,request("Login successful")
        else:
            messages.success,request("impossible kiongozi fikiria tena ")
    else:
        return render(request,'login/ingia.html')
    
def logout(request):
    logout(request)
    return redirect ('home')

def home(request):
    return render(request,'login/home.html')