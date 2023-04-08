from django.contrib import admin

# Register your models here.

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'user', 'price', 'description', 'activity_id', 'category_id', 'specialization_id']
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Order, OrderAdmin)
