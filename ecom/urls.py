
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.forms import CustomLoginForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.auth_login, name='login', kwargs={ "authentication_form": CustomLoginForm }),


]


