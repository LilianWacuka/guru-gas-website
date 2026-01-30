from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
def loginform(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            messages.success(request,(" uko fiti naona umerudi"))
            login(request,user)
        else:
            messages.success(request,("toa ujinga apa buda"))     
    return render(request,'login/loginform.html')


def logout(request):
    logout(request)
    messages.success(request,"Umetoka thi ukiumaga")
    return render(request,"login/home.html")

def home(request):
    return render(request,'login/home.html')