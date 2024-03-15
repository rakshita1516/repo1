"""
URL configuration for goodluck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.show),
    path('test/pqr/', views.display),
    path('test/ctc/', views.docontact),
    path('test/fdbk/', views.dofeedback),
    path('test/pqr/xyz', views.doregister),
    path('rcv/', views.receive,name="rcv"),
    path('lgn/', views.dologin,name="lgn"),
    path('feed/',views.myfeedback,name="feed"),
    path('cnt/',views.mycontact,name="cnt"),
    path('test/ord/',views.myorder),
    path('test/piz',views.mypizza),
    path('test/bur',views.doburger),
    path('test/free',views.myfrench),
    path('test/sand',views.mysandwich),
    path('test/ice',views.myicecream),
    path('test/cafe',views.mycoffee),
    path('take/',views.respect,name="take"),
    path('rpt1/', views.logreport),
    path('rpt2/', views.signreport),
    path('rpt3/', views.contreport),
    path('rpt4/', views.fedreport),
    path('rpt5/', views.orddreport),
    
]

