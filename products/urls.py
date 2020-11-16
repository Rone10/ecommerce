from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name = 'list'),
    path('<str:slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('cart/<str:slug>/', views.CartView.as_view(), name = 'cart'),
    # path('cart/<str:slug>/', views.add_order_item, name = 'cart'),
]