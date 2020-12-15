from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from . models import Product, OrderProduct,Order
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from django.urls import reverse



class ProductsListView(ListView):
    template_name = 'products/prod_list.html'
    context_object_name = 'products'
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        qty = self.request.GET.get('q')
        print(qty)
        item = Product.objects.get(slug=kwargs['slug'])
        new_item = OrderProduct.objects.create(customer=self.request.user, product=item, quantity=qty)
        new_item.save()
        # print(new_item.order_set())
        return HttpResponseRedirect(reverse('products:cart'))


class CartView(ListView):
    template_name = 'products/cart.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = OrderProduct.objects.all().filter(customer=self.request.user).exclude(purchased=False)
        return queryset


class OrderView(View):
    def get(self, *args, **kwargs):
        customer = self.request.user
        products = OrderProduct.objects.filter(customer=customer)
        order = Order.objects.create(customer=customer)
        order.products.add(*products)
        order.ordered = True
        order.save()
        for product in products:
            product.purchased = True
        return HttpResponseRedirect(reverse('products:myorders'))


class OrdersView(ListView):
    template_name = 'products/orders.html'
    context_object_name = 'orders'
    queryset = Order.objects.all().filter(ordered=True)









# class CView(ListView):
#     template_name = 'products/orders.html'
#     context_object_name = 'orders'
#     model = OrderProduct
#
    # def get_queryset(self):
    #     queryset = OrderProduct.objects.all().filter(customer=self.request.user).exclude(ordered=True)
    #     return queryset