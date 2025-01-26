from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.

from django.views.generic import ListView # Neu
from django.views.generic import CreateView
from django.views.generic import DetailView

from .models import Stoecke, Entry

def single_slug(request, single_slug):
    stoecke = [s.stock_slug for s in Entry.objects.all()]
    if single_slug in stoecke:
        return HttpResponse(f"{single_slug} is a Stock")

    return HttpResponse(f"{single_slug} has no Stock assigend")

class StoeckeHome(ListView): 
    model = Stoecke 
    template_name = 'stoecke/stock_home.html'

class StockCreate(CreateView):
    model = Stoecke 
    template_name = 'stoecke/stock_create.html'
    fields = '__all__'
    success_url = reverse_lazy('stock_start')

class StockDetail(DetailView):
    model = Stoecke
    template_name = 'stoecke/stock_detail_view.html'

def stock_entries(request, pk):
    stock = get_object_or_404(Stoecke, pk=pk)
    items = stock.entries.all()
    return render(request, 'stoecke/stock_entries.html', {'stock': stock, 'items': items})
