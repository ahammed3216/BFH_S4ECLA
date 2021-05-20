from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserLoginForm,UserRegisterForm,EventRegistration
from django.contrib.auth import logout,authenticate,get_user_model,login
from django.contrib.auth import login as auth_login
from .models import *
from django.contrib import messages
import random

User=get_user_model()


def get_ref_code():
    return '.join(random.choices(string.ascii_lowercase + string.digits))'

def home(request):
    print("hello world")
    hai=0
    return render(request,"demo.html")

def LogoutView(request):
    logout(request)
    return redirect('/')



def LoginView(request):
    form=UserLoginForm(request.POST or None)
  
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        
        user=authenticate(username=username,password=password)
        login(request,user)
        print("hello")
        messages.info(request,"YOU ARE SUCCESSFULLY LOGIN TO YOUR ACCOUNT")
        return redirect('http://127.0.0.1:8000/')
    context={
        'form':form
    }
    print("hai")
    return render(request,"login.html",context)


def register(request):
    form=UserRegisterForm(request.POST or None)
    print("hello")
    print("hai")
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password1')
        email=form.cleaned_data.get('email')
        first_name=form.cleaned_data.get('firstname')
        last_name=form.cleaned_data.get('lastname')
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        return redirect('http://127.0.0.1:8000/login/')
    context={
        'form':form
    }
    return render(request,'signup.html',context)


def EventRegister(request):
    form=EventRegistration(request.POST ,request.FILES)
    print("hai")
    if form.is_valid():
        print("pooi")
        title=form.cleaned_data.get('title')
        event_description=form.cleaned_data.get('event_description')
        event_time=form.cleaned_data.get('event_time')
        event_venue=form.cleaned_data.get('event_venue')
        contact_number=form.cleaned_data.get('contact_number')
        contact_email=form.cleaned_data.get('contact_email')
        event_head=form.cleaned_data.get('event_head')
        event_hosted_by=form.cleaned_data.get('event_hosted_by')
        event_image=form.cleaned_data.get('event_image')
        total_seats=form.cleaned_data.get('total_seats')
        event_date=form.cleaned_data.get('event_date')
        print("hello")

        eventmodel=EventRegistartion(
            created_person=request.user,
            title=title,
            event_time=event_time,
            event_description=event_description,    
            event_venue=event_venue,
            total_seats=total_seats,
           
            event_head=event_head,
            contact_email=contact_email,
            contact_number=contact_number,
            event_hosted_by=event_hosted_by,
            event_image=event_image,
            event_date=event_date
        )
        eventmodel.save()
        print ("sucess")
        return redirect('/')
    
    print("world")

    return render(request,"event_register.html")


def DefineView(request,id):
    event=get_object_or_404(EventModel,id=id)
    context={
        'event':event
    }
    return render (request,"define.html",context)


def add_to_cart(request,id):
    event=get_object_or_404(EventModel,id=id)
    orderitem_qs=OrderEvent.objects.filter(user=request.user,events=event,booked=True)
    if orderitem_qs.exists():
        messages.info(request,"Event is already is in your profile")
        return redirect('/')
    else:
        orderitem=OrderEvent(
            user=request.user,
            events=event,
            booked=True

        )
        orderitem.save()

        ref_code=get_ref_code()
        
        orderevent=Order(
            user=request.user,    
            start_date=event.event_date,
            ref_code=ref_code
        )
        print("hello")
        orderevent.save()
        orderevent.events.add(orderitem)
        
        messages.info(request,"Event has sucessfully added to your profile")
        return redirect ('/')


def remove_from_cart(request,id):
    event=get_object_or_404(EventModel,id=id)
    orderitem_qs=OrderEvent.objects.filter(user=request.user,events=event,booked=False)
    if orderitem_qs.exists():
        messages.info(request,"Event is already is not in your your profile")
        return redirect('/')
    else:
        orderitem=OrderEvent(
            user=request.user,
            events=event,
            booked=False

        )
        orderitem.save()


        
        
        
        messages.info(request,"Event has sucessfully removed from your profile")
        return redirect ('/')

