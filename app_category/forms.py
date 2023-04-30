# # forms.py
# from django import forms
# from .models import Specialization, Category, Sphere

# class OrderForm(forms.Form):
#     specialization = forms.ModelChoiceField(queryset=Specialization.objects.all())
#     category = forms.ModelChoiceField(queryset=Category.objects.none())
#     sphere = forms.ModelChoiceField(queryset=Sphere.objects.none())

#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args, **kwargs)
#         if 'specialization' in self.data:
#             try:
#                 specialization_id = int(self.data.get('specialization'))
#                 self.fields['category'].queryset = Category.objects.filter(specialization_id=specialization_id)
#             except (ValueError, TypeError):
#                 pass
#         if 'category' in self.data:
#             try:
#                 category_id = int(self.data.get('category'))
#                 self.fields['sphere'].queryset = Sphere.objects.filter(category_id=category_id)
#             except (ValueError, TypeError):
#                 pass

# # views.py
# from django.shortcuts import render
# from .forms import OrderForm

# def order_view(request):
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
#         # обработка формы
#     return render(request, 'order.html', {'form': form})

# # order.html
# <form method="POST" action="{% url 'order_view' %}">
#   {% csrf_token %}
#   {{ form.as_p }}
#   <button type="submit">Отправить</button>
# </form>







# from django import forms
# from django.contrib.auth.models import User

# class MyForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['user'].initial = self.request.user
        
#     class Meta:
#         model = MyModel
#         fields = ['field1', 'field2', 'user']