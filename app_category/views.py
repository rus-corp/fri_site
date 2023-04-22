from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from app_users.models import CustomUser




from .models import Activity, Categoryes, Specialization, SpecializationUser

def main_view(request, activity=None, category=None, specialization=None):
    activity_list = Activity.objects.all()
    category_list = None
    user_id = int(request.user.id)
    myuser = CustomUser.objects.filter(pk=user_id).first()
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
    if specialization:
        specialation_choice = Specialization.objects.get(slug=specialization)
        SpecializationUser.objects.create(users=, specialization=specialation_choice)
        specializtions = SpecializationUser.objects.filter(users_id=user_id)
        context['specializations_choice'] = specializtions


    return render(request, 'app_category/category.html', context)

