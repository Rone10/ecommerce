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
        # login(self.request, self.object)
        # # get the username and password
        # username = self.request.POST[ 'email' ]
        # password = self.request.POST[ 'password1' ]
        # # # authenticate user then login
        # user = authenticate(username=username, password=password)
        user = authenticate(
            username=form.cleaned_data[ "email" ],
            password=form.cleaned_data[ "password1" ],
        )
        # username = form.cleaned_data[ "username"]
        # password = form.cleaned_data[ "password1"]
        # user={'username':username, 'password': password  }
        login(self.request, user)
        return HttpResponseRedirect('address/')

class AddressView(CreateView):
    form_class = AddressForm
    model = Address
    template_name = 'users/address.html'
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

