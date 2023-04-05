from django.contrib import admin

# Register your models here.

from .models import Activity, Categoryes, Specialization


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CategoryesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activity']

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']



admin.site.register(Activity, ActivityAdmin)
admin.site.register(Categoryes, CategoryesAdmin)
admin.site.register(Specialization, SpecializationAdmin)