from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# Register your models here.

from .models import Specializtion, Categories


class SpecializationAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Specializtion, SpecializationAdmin)
admin.site.register(Categories, CategoryAdmin)

