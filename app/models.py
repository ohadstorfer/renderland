from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def _str_(self):
        return self.description



class Product(models.Model):
    description = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category= models.ForeignKey(Category,on_delete= models.CASCADE, null= True)
 
    def __str__(self):
           return self.description
    



   
