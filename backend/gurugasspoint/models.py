from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    weight=models.IntegerField()
    price=models.IntegerField()
    units=models.IntegerField()
    serial_number=models.CharField(max_length=100)
    
    
class Order(models.Model):
    Customer_name=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    weight=models.IntegerField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    
class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    location=models.CharField(max_length=80)
    
class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)