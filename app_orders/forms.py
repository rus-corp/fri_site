from django.forms import ModelForm, TextInput
from .models import Order

class CreateOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'description', 'price', 'activity', 'category', 'specialization']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input'}),
            'description': TextInput(attrs={'cols': 40, 'rows': 8})
        }