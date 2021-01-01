from django.forms.widgets import PasswordInput, EmailInput, TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import User, Address

email_classes = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
password_classes = "shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
text_classes = "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"
password_classes = "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(widget=TextInput(attrs={'class': text_classes,
                                                         'id': 'first_name',
                                                         'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=TextInput(attrs={ 'class': text_classes,
                                                        'id': 'lasts_name',
                                                        'placeholder': 'Last Name' }))
    email = forms.CharField(widget=EmailInput(attrs={ 'class': text_classes,
                                                      'placeholder': 'Email',
                                                      'id': 'email' }))
    username = forms.CharField(widget=TextInput(attrs={ 'class': text_classes,
                                                        'id': 'username',
                                                        'placeholder': 'Username' }))
    password1 = forms.CharField(widget=PasswordInput(attrs={ 'class': password_classes,
                                                             'placeholder': 'Password',
                                                             'id': "password1" }))

    password2 = forms.CharField(widget=PasswordInput(attrs={ 'class': password_classes,
                                                             'placeholder': 'Re-type Password',
                                                             'id': "password2" }))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')



class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(widget=EmailInput(attrs={'class':email_classes,'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': password_classes,'placeholder':'Password',  'id':"password"}))


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'address_2', 'city', 'postal_code', 'country']
