from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from . models import Product, OrderProduct,Order
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, HttpResponse
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductsListView(ListView):
    template_name = 'products/prod_list.html'
    context_object_name = 'products'
    model = Product
    #Needs pagination

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class CreateOrderView(View):

    def get(self, *args, **kwargs):
        customer = self.request.user
        products = OrderProduct.objects.all().filter(ordered=False)
        order = Order.objects.create(customer=customer)
        if products.exists():
            for product in products:       
                product.ordered = True
                product.removed_from_cart = True
                product.save()
                order.products.add(product)
        order.ordered = True 
        order.save()
        print('***Checking OrderProduct status****')
        for product in OrderProduct.objects.all():
            print(f'{product.product.name} - Ordered: {product.ordered} Removed: {product.removed_from_cart}')
        return HttpResponseRedirect(reverse('products:checkout'))
        

class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        qty = int(self.request.GET.get('q'))
        print(qty)
        item = Product.objects.get(id=kwargs['id'])
        try:
            checked_item = OrderProduct.objects.get(product=item, ordered=False)
            if checked_item:
                prev_qty = checked_item.quantity 
                checked_item.quantity = prev_qty+qty
                checked_item.save()
            return HttpResponseRedirect(reverse('products:cart'))
        except:   
            new_item = OrderProduct.objects.create(product=item, quantity=qty, customer=self.request.user)
            new_item.save()
        return HttpResponseRedirect(reverse('products:cart'))

 
class CheckoutView(TemplateView):
     template_name = 'products/checkout.html'


class ContactView(TemplateView):
     template_name = 'products/contact.html'


class CartView(ListView):
    template_name = 'products/cart.html'
    context_object_name = 'items'
    queryset = OrderProduct.objects.all().exclude(ordered=True)

 
class OrdersView(ListView):
    template_name = 'products/orders.html'
    context_object_name = 'orders'
    queryset = Order.objects.all().filter(ordered=True)


class OrdersView(LoginRequiredMixin, ListView):
    template_name = 'products/orders.html'
    context_object_name = 'orders'

    def get_queryset(self): 
        return Order.objects.all().filter(customer=self.request.user, ordered=True)

