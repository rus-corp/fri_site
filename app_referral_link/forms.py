from django.forms import ModelForm
from .models import Get_referral


class CreateGet_referral(ModelForm):
    class Meta:
        model = Get_referral
        fields = ['name', 'email', 'choice_of_specialty', 'file1', 'file2', 'file3', 'file4', 'file5']
