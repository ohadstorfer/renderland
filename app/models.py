from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    img = models.ImageField()
    category= models.ForeignKey(Category,on_delete= models.CASCADE, null= True)
 
    def __str__(self):
           return self.desc
    



class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now_add=True) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'oreder {self.id}'
    
class OrederDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey    
    



   
