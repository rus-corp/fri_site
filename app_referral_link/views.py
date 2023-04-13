from celery.worker import request
from django.views.generic import ListView, CreateView
from .forms import CreateGet_referral


class CreateGet_referralView(CreateView):
    form_class = CreateGet_referral
    template_name = 'app_referral_link/create_rl1.html'
    success_url = 'success/'
