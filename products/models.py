from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    verbose_name_plural = "Categories"


class Product(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()
    price= models.DecimalField(max_digits=8,decimal_places=3)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active= models.BooleanField(default=True)
    date_time = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name ='prodect'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    def __str__(self):
        return self.user.username
    def calculate_total(self):
        total = 0
        items = self.itempanier_set.all()
        for item in items:
            total += item.product.price * item.quantity
        return total


class ItemPanier(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.product.name)
    

class Orders_Confirm(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    