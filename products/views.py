from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from . models import Product, OrderProduct,Order, Cart
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, HttpResponse
from django.urls import reverse



class ProductsListView(ListView):
    template_name = 'products/prod_list.html'
    context_object_name = 'products'
    model = Product
    #Needs pagination

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        item = Product.objects.get(slug=kwargs['slug'])
        Cart.objects.create(product=item)
        return HttpResponseRedirect(reverse_lazy('products:cart'))
 
 
class CheckoutView(TemplateView):
     template_name = 'products/checkout.html'


class CartView(ListView):
    template_name = 'products/cart.html'
    context_object_name = 'items'
    queryset = Cart.objects.all()


from django.core.exceptions import ObjectDoesNotExist




class CreateOrderView(View):
    def get(self, *args, **kwargs):
        customer = self.request.user
        if Cart.objects.exists():
            order = Order.objects.create(customer=customer)
            for item in Cart.objects.all():
                order_product = OrderProduct.objects.create(product=item.product, quantity=item.quantity) 
                order_product.save() 
                order.products.add(order_product)
                Cart.objects.filter(product=item.product).delete()
            order.ordered=True
            order.save()
        return HttpResponseRedirect(reverse('products:checkout'))
# class CreateOrderView(View):
#     def get(self, *args, **kwargs):
#         customer = self.request.user
#         if Cart.objects.exists():
#             order = Order.objects.create(customer=customer)

#             for item in Cart.objects.all():  #new code
#                 item.products.purchased = True #new code
#                 order.products.add(item.products)
#                 Cart.objects.filter(products=item.products).delete()
#             order.ordered=True
#             order.save()

#         return HttpResponseRedirect(reverse('products:checkout'))


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