from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def show(request):
   return render(request,'index.html')

def mypizza(request):
   return render(request,'pizza.html')

def doburger(request):
   return render(request,'burger.html')

def myfrench(request):
   return render(request,'French Fire.html')

def mysandwich(request):
   return render(request,'sandwich.html')

def myicecream(request):
   return render(request,'icecream.html')

def mycoffee(request):
   return render(request,'coffee.html')

def display(request):
   return render(request,'login.html')

def doregister(request):
   return render(request,'signup.html')

def myorder(request):
   return render(request,'order.html')

def docontact(request):
   return render(request,'contact.html')

def dofeedback(request):
   return render(request,'feedback.html')

def logreport(request):
   log=Login.objects.all()
   return render(request,'report1.html',{'log':log})

def signreport(request):
   sign=Signup.objects.all()
   return render(request,'report2.html',{'sign':sign})

def contreport(request):
   cont=Contact.objects.all()
   return render(request,'report3.html',{'cont':cont})

def fedreport(request):
   fed=Feedback.objects.all()
   return render(request,'report4.html',{'fed':fed})

def orddreport(request):
   ordd=Order.objects.all()
   return render(request,'report5.html',{'ordd':ordd})


def receive(request):
  if request.method=="POST":
     name=request.POST.get('name')
     password=request.POST.get('pwd')
     email=request.POST.get('email')
     z=Signup(name=name,email=email,password=password)
     z.save()
     return HttpResponse("<h1>Data Entered</h1>")
  else:
     return HttpResponse("<h1>Invalid Request</h1>")

def dologin(request):
  if request.method=="POST":
     username=request.POST.get('name')
     password=request.POST.get('pwd')
     z=Login(username=username,password=password)
     z.save()
     return HttpResponse("<h1>Data Entered</h1>")
  else:
     return HttpResponse("<h1>Invalid Request</h1>")


def respect(request):
  if request.method=="POST":
     name=request.POST.get('name')
     phone=request.POST.get('phone')
     extra=request.POST.get('ex')
     address=request.POST.get('add')
     email=request.POST.get('email')
     foodname=request.POST.get('food')
     howmuch=request.POST.get('how')
     message=request.POST.get('msg')
     z=Order(name=name,phone=phone,extra=extra,address=address,email=email,foodname=foodname,howmuch=howmuch,message=message)
     z.save()
     return HttpResponse("<h1>Data Entered</h1>")
  else:
     return HttpResponse("<h1>Invalid Request</h1>")


def myfeedback(request):
   if request.method=="POST":
     name=request.POST.get('fedname')
     email=request.POST.get('fedemail')
     message=request.POST.get('message')
     z=Feedback(name=name,email=email,message=message)
     z.save()
     return HttpResponse("<h1>Data Entered</h1>")
   else:
     return HttpResponse("<h1>Invalid Request</h1>")

def mycontact(request):
   if request.method=="POST":
     username=request.POST.get('username')
     email=request.POST.get('email')
     website=request.POST.get('website')
     mobileno=request.POST.get('mobileno')
     z=Contact(username=username,email=email,website=website,mobileno=mobileno)
     z.save()
     return HttpResponse("<h1>Data Entered</h1>")
   else:
     return HttpResponse("<h1>Invalid Request</h1>")





