# from django.contrib import admin
# from django.urls import path
# from Amazon.views import home

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', home),
# ]

# from django.urls import path
# from Amazon.views import home

# urlpatterns = [
#    path('', home),
# ]
# from django.contrib import admin
# from django.urls import path
# from .views import * ## Importing all views from the current app's views.py file

# urlpatterns = [
#     path('categorie', category_products, name='category_products'),
# ]


from django.contrib import admin
from django.urls import path
from .views import * ## Importing all views from the current app's views.py file

urlpatterns = [
    path('categorie', category_products, name='category_products'),
    path('products', product_list, name='products_list'),
]
