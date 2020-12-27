from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name = 'list'),
    path('checkout/', views.CheckoutView.as_view(), name = 'checkout'),
    path('mycart/', views.CartView.as_view(), name = 'cart'),
    path('order/', views.CreateOrderView.as_view(), name = 'order'),
    path('view_orders/', views.OrdersView.as_view(), name = 'myorders'),
    path('<str:slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('add/<str:slug>/', views.AddToCartView.as_view(), name = 'add_to_cart'),

    # path('add/<int:pk>/', views.AddToCartView.as_view(), name = 'add_to_cart'),

]
