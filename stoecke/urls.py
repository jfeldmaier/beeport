# stoecke/urls.py

from django.urls import path
from .views import StoeckeHome
from .views import StockCreate
from .views import StockDetail
from .views import stock_entries

urlpatterns = [
             path('', StoeckeHome.as_view(), name='stock_start'),
             path('new/', StockCreate.as_view(), name='new_stock'),
             path('<int:pk>/', stock_entries, name='stock_entries'),
             path('update/<int:pk>/', StockDetail.as_view(), name='stock_detail'),
             ]
