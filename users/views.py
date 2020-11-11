from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from . forms import UserCreateForm
from . models import User
# Create your views here.

def index(request):
    return HttpResponse('hello world!!')

class UserSignup(CreateView):
    form_class = UserCreateForm
    model = User
    template_name = 'users/signup.html'
    success_url = '/'
