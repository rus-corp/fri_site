from django.contrib import admin

# Register your models here.

from .models import Order, OrderExecCust

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'customer', 'name', 'price', 'description', 'status', 'category_id', 'specialization_id']
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Order, OrderAdmin)

class OrderExecutAdmin(admin.ModelAdmin):
    model = OrderExecCust
    list_display = ['id', 'order', 'executor']