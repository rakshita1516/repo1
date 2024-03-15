from django.contrib import admin
from .models import *
# Register your models here.

class SignupAdmin(admin.ModelAdmin):
  list_display=['name','email','password']
class LoginAdmin(admin.ModelAdmin):
  list_display=['username','password']
class OrderAdmin(admin.ModelAdmin):
  list_display=['name','phone','extra','address','email','foodname','howmuch','message']
class ContactAdmin(admin.ModelAdmin):
  list_display=['username','email','website','mobileno']
class FeedbackAdmin(admin.ModelAdmin):
  list_display=['name','email','message']

admin.site.register(Signup,SignupAdmin)

admin.site.register(Login,LoginAdmin)

admin.site.register(Order,OrderAdmin)

admin.site.register(Contact,ContactAdmin)

admin.site.register(Feedback,FeedbackAdmin)

