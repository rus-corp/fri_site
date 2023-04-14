from celery.worker import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import CreateGet_referral
from django.http import HttpResponse


def upload_view(request):
    return render(request,'app_referral_link/success.html')


class CreateGet_referralView(CreateView):
    form_class = CreateGet_referral
    template_name = 'app_referral_link/create_rl1.html'
    success_url = reverse_lazy('uploaded')
    
    
    
    
    
