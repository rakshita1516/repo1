from django.db import models

# Create your models here.
class Signup(models.Model):
   name=models.CharField(max_length=25)
   email=models.CharField(max_length=20)
   password=models.CharField(max_length=15)

class Login(models.Model):
   username=models.CharField(max_length=25)
   password=models.CharField(max_length=15)

class Order(models.Model):
  name=models.CharField(max_length=25)
  phone=models.IntegerField(null=True)
  extra=models.CharField(max_length=25)
  address=models.TextField()
  email=models.CharField(max_length=25)
  foodname=models.CharField(max_length=25)
  howmuch=models.IntegerField()
  message=models.TextField()

class Contact(models.Model):
   username=models.CharField(max_length=25)
   email=models.CharField(max_length=25)
   website=models.CharField(max_length=25)
   mobileno=models.IntegerField(null=True)

class Feedback(models.Model):
   name=models.CharField(max_length=25)
   email=models.CharField(max_length=20)
   message=models.CharField(max_length=15)  