from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from . forms import UserCreateForm, AddressForm
from . models import User, Address
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return HttpResponse('hello world!!')

class UserSignup(CreateView):
    form_class = UserCreateForm
    model = User
    template_name = 'users/signup.html'
    success_url = 'address/'

    def form_valid(self, form):
        # save the new user first
        form.save()
         # get the username and password
        user = authenticate(
            username=form.cleaned_data[ "email"],
            password=form.cleaned_data[ "password1"],
        )
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class AddressView(CreateView):
    form_class = AddressForm
    model = Address
    template_name = 'users/address.html'
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

