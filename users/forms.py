from django.forms.widgets import PasswordInput, EmailInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


email_classes = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
password_classes = "shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(widget=EmailInput(attrs={'class':email_classes,'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': password_classes,'placeholder':'Password',  'id':"password"}))
