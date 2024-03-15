from django.db import models

# Create your models here.

class Customer(models.Model):
   cust_id=models.IntegerField()
   name=models.CharField(max_length=20)
   location=models.CharField(max_length=20)
   order_id=models.IntegerField()

