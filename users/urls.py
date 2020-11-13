from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='home' ),
    path('signup', views.UserSignupView.as_view(), name='signup'),
    path('address/', views.AddressView.as_view(), name='address'),
]