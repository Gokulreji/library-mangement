from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib import messages
from. models import *


def login(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        p=request.POST.get("password")
        user=authenticate(username=uname,password=p)
        if user is not None:
            if user.is_superuser:
                dj_login(request,user)
                return redirect('addbook')
        else:
            messages.info(request,'invalid user')
    return render(request,'login.html')


def addbook(request):
    if request.method == "POST" and request.FILES['file']:
        name = request.POST.get('name')
        number = request.POST.get('number')
        price = request.POST.get('price')
        file = request.POST.get('file')
        BookDetails.objects.create(name = name,number = number, price = price,file = file)
        return redirect('addbook')
    return render(request, 'addbook.html')

def showbook(request):
    book = BookDetails.objects.all()
    return render(request,'showbook.html',{'books':book})

def delete(request,book_id):
    item = BookDetails.objects.get(id = book_id)
    item.delete()
    return redirect('showbook')



# Create your views here.
