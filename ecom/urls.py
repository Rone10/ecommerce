
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.forms import CustomLoginForm
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('products/', include(('products.urls', 'products'), namespace= 'products')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.auth_login, name='login', kwargs={ "authentication_form": CustomLoginForm }),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
