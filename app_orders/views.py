from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Order
from .forms import CreateOrder
# Create your views here.


#создание заказа
class CreateOrderView(CreateView):
    form_class = CreateOrder
    template_name = 'app_users/others/place_contract.html'
    success_url = reverse_lazy('orders')
    


#вывод всех заказов
class OrdersView(ListView):
    model = Order
    template_name = 'app_users/others/contracts.html'


