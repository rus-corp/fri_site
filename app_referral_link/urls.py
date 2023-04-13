from django.urls import path

from .views import CreateGet_referralView

urlpatterns = [
    path('', CreateGet_referralView.as_view(), name='referral_link'),
    path('success', CreateGet_referralView.as_view(), name='success'),
]