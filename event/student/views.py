from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth import logout,authenticate,get_user_model,login
from django.contrib.auth import login as auth_login

User=get_user_model()

def home(request):
    print("hello world")
    hai=0
    return render(request,"demo.html")


def LoginView(request):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        print("hello")
        return redirect('/')
    context={
        'form':form
    }
    print("hai")
    return render(request,"login.html",context)


def register(request):
    form=UserRegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password1')
        email=form.cleaned_data.get('email')
        first_name=form.cleaned_data.get('first_name')
        last_name=form.cleaned_data.get('last_name')
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        return redirect('http://127.0.0.1:8000/login/')
    context={
        'form':form
    }
    return render(request,'register.html',context)