from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Checkout_details(models.Model):
    name=models.CharField(max_length=220)
    address=models.TextField()
    zip=models.CharField(max_length=3)
    phone=models.CharField(max_length=10)
    payment_method = models.CharField(max_length=20, choices=
    [
        ('cashOnDelivery', 'Cash on Delivery'),
        ('cardPayment', 'Card Payment')
    ])
    cardnumber=models.IntegerField(blank=True, null=True)
    cvv=models.CharField(max_length=16,blank=True, null=True)
    expirydate=models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    product_name=models.CharField(max_length=220,null=True)
    author_name=models.CharField(max_length=220,null=True)
    price=models.FloatField()
    image=models.ImageField(null=True)
    def __str__(self):
        return self.product_name
    

class Order_item(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def total_price(self):
        return self.quantity * self.product.price
