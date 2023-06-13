#from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

# Create your views here.
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'object_list'
