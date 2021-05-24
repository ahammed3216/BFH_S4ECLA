from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserLoginForm,UserRegisterForm,EventRegistration,img_test_form
from django.contrib.auth import logout,authenticate,get_user_model,login
from django.contrib.auth import login as auth_login
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import random

User=get_user_model()


def get_ref_code():
    return '.join(random.choices(string.ascii_lowercase + string.digits))'



def home(request):
        items=EventModel.objects.filter(approve_admin=True)
        print("hello world")
        hai=0
        array1=["card current--card","ard next--card","card previous--card"]
        context={
            'items':items,
            'styles1':array1
        }
        return render(request,"index.html",context)

def LogoutView(request):
    logout(request)
    messages.info(request,"You are successfully logout from your account")
    return redirect('/home')



def LoginView(request):
    if request.method =="POST":
        form=UserLoginForm(request.POST)
            
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            user=authenticate(username=username,password=password)
            login(request,user)
            print("hello")
            messages.info(request,"YOU ARE SUCCESSFULLY LOGIN TO YOUR ACCOUNT")
            return redirect('/home')
        else:
            return render(request,"login.html",{'form':form})         
    else:
        form=UserLoginForm()
    return render(request,"login.html")


def register(request): 
    print("hai")
    if request.method=="POST":
        print("hello")
        form=UserRegisterForm(request.POST)
        print("worls")
        if form.is_valid():       
            print("bye")
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')
            email=form.cleaned_data.get('email')
            first_name=form.cleaned_data.get('firstname')
            last_name=form.cleaned_data.get('lastname')
            user=User.objects.create_user(username,email,password)
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            messages.info(request,"your profile is successfully registered")
            return redirect('/login/')
        else:
            print("no")
            return render(request,"signup.html",{'form':form})
    else:
        form=UserRegisterForm()          
    return render(request,'signup.html')


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

        eventmodel=EventModel(
            created_person=request.user,
            title=title,
            event_time=event_time,
            event_description=event_description,    
            event_venue=event_venue,
            total_seats=total_seats,
            available_seats=total_seats,
            event_head=event_head,
            contact_email=contact_email,
            contact_number=contact_number,
            event_hosted_by=event_hosted_by,
            
            event_date=event_date,
            approve_admin=False
        )
        eventmodel.save()
        print ("sucess")
        return redirect('/home')
    
    print("world")

    return render(request,"event_register.html")


def DefineView(request,id):
    event=get_object_or_404(EventModel,id=id)
    items=OrderEvent.objects.filter(events=event,booked=True)
   
    context={
        'event':event,
        'items':items
    }
    return render (request,"event_description.html",context)


def add_to_cart(request,id):
    if request.user.is_authenticated:
        event=get_object_or_404(EventModel,id=id)
        orderitem_qs=OrderEvent.objects.filter(user=request.user,events=event,booked=True)
        if orderitem_qs.exists():
            messages.info(request,"Event is already is in your profile")
            return redirect('/home')
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
            ordermodel=EventModel.objects.get(id=id)
            available_seats=ordermodel.available_seats
            ordermodel.available_seats=available_seats - 1
            ordermodel.save()
            
            messages.info(request,"Event has sucessfully added to your profile")
            return redirect ('/home')
    else:
        messages.info(request,"you must login to your account to perform this task")
        return redirect("/login")


def remove_from_cart(request,id):
    if request.user.is_authenticated:
        event=get_object_or_404(EventModel,id=id)
        orderitem_qs=OrderEvent.objects.filter(user=request.user,events=event,booked=False)
        if orderitem_qs.exists():
            messages.info(request,"Event is already is not in your your profile")
            return redirect('/home')
        else:
            orderitem=OrderEvent(
                user=request.user,
                events=event,
                booked=False

            )
            orderitem.save()

            ordermodel=EventModel.objects.get(id=id)
            available_seats=ordermodel.available_seats
            ordermodel.available_seats=available_seats + 1
            ordermodel.save()
            
            
            
            
            messages.info(request,"Event has sucessfully removed from your profile")
            return redirect ('/home')
    else:
        messages.info(request,"you must login to your account to perform this task")
        return redirect("/login")




def ErrorView(request):
    return render(request,"error.html")

def profile(request):
    man=request.user
    items=OrderEvent.objects.filter(user=request.user,booked=True)
    context={
        'items':items,
        'man':man
    }
    return render(request,"profile.html",context)

def img_test(request):
    if request.method == "POST":
        form=img_test_form()
        if form.is_valid():
            print('heloo')
            img=form.cleaned_data.get('img')
            test=img_test(img=img)
            test.save()
            return redirect(request,'/home')
        else:
            print("hello")
            return redirect('/error')
    else:
        form=img_test_form()
        print("hai")
        return render(request,"img_test.html",{'form':form})

