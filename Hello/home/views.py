from django.shortcuts import render,HttpResponse
from matplotlib.style import context
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import signupform


def index(request):
    # return HttpResponse('this is home page')
    context={
        'variable':'kishan is great'
    }
    
    return render(request,'index.html',context)
    

def about(request):
    # return HttpResponse('this is about page')
    return render(request,'about.html')

def services(request):
    # return HttpResponse('this is services page')
    return render(request,'services.html')
    
def contact(request):
    # return HttpResponse('this is contact page')
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your response has been recorded!')
    return render(request,'contact.html')



# login,signup

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')


def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:            
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')

    return render(request,'login.html')

def signupview(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login') 
    else:
        form=signupform()

    return render(request,'signup.html',{'form':form})


def logoutuser(request):
    logout(request)
    return redirect("/login")
