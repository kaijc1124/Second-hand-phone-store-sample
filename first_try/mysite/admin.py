from django.contrib import admin
from mysite.models import Post
from mysite.models import Phone_Maker
from mysite.models import Phone_Model
from mysite.models import Phone_Product
from mysite.models import Phone_Product2
from mysite.models import Users
from mysite.models import Email
from mysite.models import born111
from mysite.models import phone_cart
from mysite.models import phone_shopped2

# Register your models here.

admin.site.register(Post)
admin.site.register(Phone_Maker)
admin.site.register(Phone_Model)
admin.site.register(Phone_Product)
admin.site.register(Phone_Product2)
admin.site.register(Email)

class userDisplay(admin.ModelAdmin):
    list_display=("User_account","email")

admin.site.register(Users,userDisplay)

class babyDisplay(admin.ModelAdmin):
    list_display=("City","Sum","Male","Female")

admin.site.register(born111,babyDisplay)

class pcartDisplay(admin.ModelAdmin):
    list_display=("User_account","pid")

admin.site.register(phone_cart,pcartDisplay )

class shoppedDisplay(admin.ModelAdmin):
    list_display=("User_account","pid","quantity","phone_number","address","paid")

admin.site.register(phone_shopped2,shoppedDisplay)