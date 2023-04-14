from django.urls import path

from .views import CreateGet_referralView, upload_view

urlpatterns = [
    path('uploaded/', upload_view, name='uploaded'),
    path('', CreateGet_referralView.as_view(), name='referral_link'),
    
]
