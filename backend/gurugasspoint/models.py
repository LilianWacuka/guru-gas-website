from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    weight=models.IntegerField()
    price=models.IntegerField()
    units=models.IntegerField()
    serial_number=models.CharField(max_length=100)
    def __str__(self):
        return self.product_name
    
    
class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    weight=models.IntegerField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    def __str__(self):
        return self.customer_name
    
class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    location=models.CharField(max_length=80)
    def __str__(self):
        return self.customer_name
    
class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.username