from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from products.models import Cart

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username


class Breeders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    milk_quantity = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    
    def add_milk_quantity(self, quantity):
        self.milk_quantity += quantity
        
    def update_balance(self, milk_quantity, liter_price):
        self.balance += milk_quantity * liter_price
   
    def make_payment(self, milk_quantity, balance):
        self.milk_quantity = milk_quantity
        self.balance = balance
        self.save()

        Breeder_payment.objects.create(
            breeders=self,
            milk_quantity=milk_quantity,
            balance=balance,
            date_time=datetime.now()
        )

        # Réinitialiser les champs milk_quantity et balance à zéro
        self.milk_quantity = 0
        self.balance = 0
        self.save()

    def __str__(self):
        return self.user.username
    
    
class Delivery(models.Model):
    breeders = models.ForeignKey(Breeders, on_delete=models.CASCADE, related_name='deliveries')
    date_time = models.DateTimeField(default=datetime.now)
    milk_quantity = models.FloatField(default=0,validators=[MinValueValidator(0.1)])
    liter_price = models.FloatField(default=3,validators=[MinValueValidator(0.1)])


class Breeder_payment(models.Model):
    breeders=models.ForeignKey(Breeders, on_delete=models.CASCADE)
    milk_quantity = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):    
        return self.breeders.user.username




    