from django.db import models


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('pub_date',)

    def __str__(self):
        return self.title


class Phone_Maker(models.Model):
    Maker=models.CharField(max_length=200)
    Country=models.CharField(max_length=200)

    def __str__(self):
        return self.Maker

class Phone_Model(models.Model):
    Maker=models.ForeignKey(Phone_Maker,on_delete=models.CASCADE)
    Model=models.CharField(max_length=200)
    URL=models.URLField()

    def __str__(self):
        return self.Model

class Phone_Product(models.Model):
    Model=models.ForeignKey(Phone_Model,on_delete=models.CASCADE)
    Description=models.CharField(max_length=200)
    Price=models.PositiveIntegerField()
    Quantity=models.PositiveIntegerField()
    Img=models.URLField()
    Owner=models.CharField(max_length=20)
    class Meta:
        ordering=('Model',)

    def __str__(self):
        return self.Description

class Phone_Product2(models.Model):
    Model=models.ForeignKey(Phone_Model,on_delete=models.CASCADE)
    Description=models.CharField(max_length=200)
    Price=models.PositiveIntegerField()
    Quantity=models.PositiveIntegerField()
    Img=models.ImageField(upload_to='image/')
    Owner=models.CharField(max_length=20)
    class Meta:
        ordering=('Model',)

    def __str__(self):
        return self.Description

class Email(models.Model):
    email=models.CharField(max_length=30)

    def __str__(self):
        return self.email

class Users(models.Model):
    User_account=models.CharField(max_length=20)
    User_password=models.CharField(max_length=20)
    email=models.ForeignKey(Email,on_delete=models.CASCADE)

    def __str__(self):
        return self.User_account


class born111(models.Model):
    City=models.CharField(max_length=3)
    Sum=models.PositiveIntegerField()
    Male=models.PositiveIntegerField()
    Female=models.PositiveIntegerField()

    class Meta:
        ordering=("id",)

    def __str__(self):
        return self.City

class phone_cart(models.Model):
    User_account = models.CharField(max_length=20)
    pid=models.PositiveIntegerField()

    class Meta:
        ordering=("User_account",)

    def __str__(self):
        return self.User_account

class phone_shopped(models.Model):
    User_account = models.CharField(max_length=20)
    pid=models.PositiveIntegerField()
    address=models.CharField(max_length=50)
    phone_number=models.PositiveIntegerField()

    class Meta:
        ordering=("pid",)

    def __str__(self):
        return self.User_account

class phone_shopped2(models.Model):
    User_account = models.CharField(max_length=20)
    pid=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    address=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    paid=models.CharField(max_length=5,default="No")

    class Meta:
        ordering=("pid",)

    def __str__(self):
        return self.User_account