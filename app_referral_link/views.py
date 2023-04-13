from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import CreateGet_referral
from .models import Get_referral


class CreateGet_referralView(CreateView):
    form_class = CreateGet_referral
    template_name = 'app_referral_link/create_rl1.html'
    success_url = 'success'
    # print('запрос на вступление', form_class)
    # def cr_ref_link(self):
    #     print('запрос на вступление')
    #     pass