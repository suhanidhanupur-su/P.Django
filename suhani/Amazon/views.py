# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#    return HttpResponse("Hello, Django!")


from django.shortcuts import render
from .models import *  ## Importing all models from the current app's models.py file

def category_products(request):
    categories = Category.objects.prefetch_related('products').all()
    return render(request, 'category_products.html', {'categories': categories})

