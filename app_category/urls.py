from django.urls import path

from app_category.views import main_view

urlpatterns = [
    path('', main_view, name='categories-main',),
    path('<str:activity>/', main_view, name='activ'),
    path('<str:activity>/<str:category>/', main_view, name='categ'),
]