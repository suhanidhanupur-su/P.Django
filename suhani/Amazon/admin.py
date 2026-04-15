# from django.contrib import admin

# # Register your models here.
# # Register your models here.

# from django.contrib import admin
# from .models import Product

# admin.site.register(Product)


# from django.contrib import admin
# from .models import Category, Product, Student

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Student)


from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)


