# adressen/urls.py

from django.urls import path
from .views import StoeckeHome

urlpatterns = [
             path('', StoeckeHome.as_view(), name='stock_start'),
             ]
