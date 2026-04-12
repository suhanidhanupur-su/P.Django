# from django.contrib import admin
# from django.urls import path
# from Amazon.views import home

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', home),
# ]

from django.urls import path
from Amazon.views import home

urlpatterns = [
   path('', home),
]