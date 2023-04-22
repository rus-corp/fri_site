from django.forms import ModelForm, TextInput
from .models import Order

class CreateOrder(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['activity'].empty_label = 'Категория не выбрана'
        self.fields['category'].empty_label = 'Категория не выбрана'
        self.fields['specialization'].empty_label = 'Категория не выбрана'
        
    class Meta:
        model = Order
        fields = ['name', 'description', 'price', 'activity', 'category', 'specialization']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input'}),
            'description': TextInput(attrs={'cols': 40, 'rows': 8})
        }