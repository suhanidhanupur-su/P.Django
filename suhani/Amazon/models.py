# from django.db import models

# # Create your models here.

# class Product(models.Model):
#     product_name = models.CharField(max_length=255)
#     product_price = models.DecimalField(max_digits=10, decimal_places=2)
#     product_description = models.TextField()
#     product_image = models.ImageField(upload_to='products/')

#     def __str__(self):
#         return self.product_name
    
from django.db import models

# Student Model (optional - practice ke liye)
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

