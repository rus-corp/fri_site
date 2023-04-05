from django.contrib import admin

# Register your models here.

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'user', 'price', 'description']



admin.site.register(Order)