from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from . models import Product, OrderProduct
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class ProductsListView(ListView):
    template_name = 'products/prod_list.html'
    context_object_name = 'products'
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class CartView(View):

    def get(self, request, *args, **kwargs):
        qty = self.request.GET.get('q')
        print(qty)
        item = Product.objects.get(slug=kwargs['slug'])
        new_item = OrderProduct.objects.create(customer=self.request.user, product=item, quantity=qty)
        new_item.save()

        return HttpResponseRedirect(reverse('products:list'))

# def add_order_item(request, slug):
#     qty = request.GET.get('q')
#     item = Product.objects.get(slug=slug)
#     new_item = OrderProduct.objects.create(customer=request.user, product=item, quantity=qty)
#     new_item.save()
#     return HttpResponseRedirect('')
