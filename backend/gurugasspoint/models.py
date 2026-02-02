from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    weight=models.IntegerField()
    price=models.IntegerField()
    units=models.IntegerField()
    serial_number=models.CharField(max_length=100)
    product_image = models.ImageField(default="Capture.jpg",blank=True)
    def __str__(self):
        return self.product_name
    

# Mambo Ya cart Pale
class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()

    def __str__(self):
        return f"Order #{self.id} - {self.created_at}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()  # snapshot of product price at purchase time

    def total_price(self):
        return self.price * self.quantity

# mambo ya customer pale
class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    cell=models.CharField(max_length=11)
    location=models.CharField(max_length=20)    
    customer_image = models.ImageField(default="customer.png",blank=True)
    username=models.CharField(max_length=23)
    password=models.CharField(max_length=10)
    
    def __str__(self):
        return self.customer_name