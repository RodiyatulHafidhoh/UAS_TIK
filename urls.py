from django.contrib import admin
from django.urls import path
from fkip.views import indeks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', indeks, 
]
