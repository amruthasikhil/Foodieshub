from django.db import models


class ContactDb(models.Model):
     name=models.CharField(max_length=100,null=True,blank=True)
     email=models.EmailField(max_length=100,null=True,blank=True)
     subject=models.CharField(max_length=100,null=True,blank=True)
     message=models.CharField(max_length=100,null=True,blank=True)

class RegistrationDb(models.Model):
     name=models.CharField(max_length=100,null=True,blank=True)
     email=models.EmailField(max_length=100,null=True,blank=True)
     password=models.CharField(max_length=100,null=True,blank=True)
     confirm_password=models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
     username=models.CharField(max_length=50,default=True,null=True)
     productname=models.CharField(max_length=50,default=True,null=True)
     quantity=models.IntegerField(null=True,default=True)
     totalprice=models.IntegerField(null=True,default=True)
     pimg=models.ImageField(upload_to="Cart_image",null=True,blank=True)

class OrderDb(models.Model):
     Name = models. CharField(max_length=100, null=True, blank=True)
     Email = models. EmailField(max_length=100, null=True, blank=True)
     Place = models. CharField(max_length=100, null=True, blank=True)
     Address = models. CharField(max_length=100, null=True, blank=True)
     Mobile = models. IntegerField(null=True, blank=True)
     Pin = models. IntegerField(null=True, blank=True)
     TotalPrice = models. IntegerField(null=True, blank=True)
     Message = models. CharField(max_length=100, null=True, blank=True)


class FeedbackDb(models.Model):
     username = models.CharField(max_length=100, null=True, blank=True)
     Message = models. CharField(max_length=100, null=True, blank=True)

# Create your models here.
