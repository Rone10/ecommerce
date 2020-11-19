from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from . models import Product, OrderProduct,Order
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


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        qty = self.request.GET.get('q')
        print(qty)
        item = Product.objects.get(slug=kwargs['slug'])
        new_item = OrderProduct.objects.create(customer=self.request.user, product=item, quantity=qty)
        new_item.save()

        return HttpResponseRedirect(reverse('products:cart'))

# def add_order_item(request, slug):
#     qty = request.GET.get('q')
#     item = Product.objects.get(slug=slug)
#     new_item = OrderProduct.objects.create(customer=request.user, product=item, quantity=qty)
#     new_item.save()
#     return HttpResponseRedirect('')

class CartView(TemplateView):
    template_name = 'products/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            order_items = OrderProduct.objects.filter(customer=self.request.user)
            context['items'] = order_items
            return context


class OrderView(View):
    def get(self, *args, **kwargs):
        customer = self.request.user
        products = OrderProduct.objects.filter(customer=customer)
        order = Order.objects.create(customer=customer)
        order.products.add(*products)
        order.ordered = True
        order.save()
        for product in products:
            product.delete()
        return HttpResponseRedirect(reverse('products:myorders'))


class OrdersView(ListView):
    template_name = 'products/orders.html'
    context_object_name = 'orders'
    queryset = Order.objects.filter(ordered=True)


