from django.contrib import admin
from . models import User, Address
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('email',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street','city', 'country')
    list_filter = ('country',)