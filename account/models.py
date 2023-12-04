from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    options=(
        ('Mobile Phone','Mobile Phone'),
        ('Tablet','Tablet'),
        ('Smart watch','Smart watch'),
        ('Laptop','Laptop')
    )
    type=models.CharField(max_length=100,choices=options,default='Mobile Phone')
    image=models.ImageField(upload_to="product_image")
    def __str__(self):
        return self.name

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(default='cart',max_length=100)

class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(null=True)
    option=(
        ('Order Placed','Order Placed'),
        ('Shipped','Shipped'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=100,choices=option,default='Order placed')