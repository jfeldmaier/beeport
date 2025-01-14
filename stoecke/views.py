from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import ListView # Neu
from django.views.generic import CreateView

from .models import Stoecke # Neu

class StoeckeHome(ListView): # Neu
    model = Stoecke # Neu
    template_name = 'stoecke/stock_home.html' # Neu

class StockCreate(CreateView):
    model = Stoecke 
    template_name = 'stoecke/stock_create.html'
    fields = '__all__'
    success_url = reverse_lazy('stock_start')
