from django.views.generic import ListView, DetailView
from . models import Product
# Create your views here.

class ProductsListView(ListView):
    template_name = 'products/prod_list.html'
    context_object_name = 'products'
    model = Product
