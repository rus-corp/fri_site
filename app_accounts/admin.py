from django.contrib import admin

# Register your models here.
from django.contrib import admin

from app_accounts.models import Fund, Account


# Register your models here.
class FundAdmin(admin.ModelAdmin):
    list_display = ('name', 'account')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('account',)


admin.site.register(Fund, FundAdmin)
admin.site.register(Account, AccountAdmin)
