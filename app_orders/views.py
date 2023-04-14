from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Order
from .forms import CreateOrder
# Create your views here.

class CreateOrderView(CreateView):
    form_class = CreateOrder
    template_name = 'app_users/others/place_contract.html'
    success_url = 'home'




class OrdersView(ListView):
    model = Order
    template_name = 'app_users/others/contracts.html'