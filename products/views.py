from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from products.models import ProductSort



# Create your views here.


class IndexView(TemplateView):
    template_name= 'products/index.html'

class ProductlistView(ListView):
    model= ProductSort
    
    
    
    
#class ProductDetailView():
