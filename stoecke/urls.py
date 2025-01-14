# stoecke/urls.py

from django.urls import path
from .views import StoeckeHome
from .views import StockCreate

urlpatterns = [
             path('', StoeckeHome.as_view(), name='stock_start'),
             path('new/', StockCreate.as_view(), name='new_stock'),
             ]
