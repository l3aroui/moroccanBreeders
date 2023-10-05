from django.db import models
from datetime import datetime
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