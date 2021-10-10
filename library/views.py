from re import I
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout

from librarian.models import Users
from django.contrib import messages
from librarian.models import *

def login(request):
    if request.method=="POST":
        name=request.POST.get("uname")
        p=request.POST.get("password")
        user=authenticate(username=name,password=p)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
    return render(request, 'user_login.html')

def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            user = Users.objects.create(name= name, email = email,phone = phone, password = password)
            return redirect('login')
        else:
            messages.info(request,'password incorrect')

    return render(request, 'register.html')
    

def home(request):
    return render(request, 'main.html')
def buybook(request):
    book = BookDetails.objects.all()
    return render(request, 'buybook.html', {'books':book})
    