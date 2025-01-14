from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView # Neu

from .models import Stoecke # Neu

class StoeckeHome(ListView): # Neu
    model = Stoecke # Neu
    template_name = 'stoecke/stock_home.html' # Neu
