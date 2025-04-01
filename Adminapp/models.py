from django.db import models


class  CategoryDb(models.Model):
    categoryname=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    category_image=models.ImageField(upload_to="category_images",null=True,blank=True)

class ProductDb(models.Model):
    categoryname=models.CharField(max_length=50,null=True,blank=True)
    product_name=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    product_image=models.ImageField(upload_to="product_image",null=True,blank=True)

class  ServicesDb(models.Model):
    servicename=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    service_image=models.ImageField(upload_to="services_images",null=True,blank=True)

# Create your models here.
