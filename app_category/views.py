from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView




from .models import Activity, Categoryes, Specialization

def main_view(request, activity=None, category=None):
    activity_list = Activity.objects.all()
    category_list = None
    if activity:
        activity_obj = Activity.objects.get(slug=activity)
        category_list = Categoryes.objects.filter(activity=activity_obj)
        # category_list = activity_obj.categoryes
    specialization_list = None
    if category:
        category_obj = Categoryes.objects.get(slug=category)
        specialization_list = Specialization.objects.filter(category=category_obj)
    context = {
        'activity_slug': activity,
        'activitys': activity_list, 
        'categorys': category_list,
        'specializations': specialization_list
    }
    return render(request, 'app_category/category.html', context)

