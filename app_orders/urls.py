from django.urls import path

from .views import OrdersView, CreateOrderView

urlpatterns = [
    path('', OrdersView.as_view(), name='orders'),
    path('create-order', CreateOrderView.as_view() ,name='create-order'),
]