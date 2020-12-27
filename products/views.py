from django.shortcuts import render
from django.views.generic import ListView
from products.models import ProductSort

# Create your views here.
class ProductlistView(ListView):
    model= ProductSort