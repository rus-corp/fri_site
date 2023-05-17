# Register your models here.
from django.contrib import admin
from app_accounts.models import Fund, Account, Operation


# Register your models here.
class FundAdmin(admin.ModelAdmin):
    list_display = ("name", "rub_account", "usd_account")


class AccountAdmin(admin.ModelAdmin):
    list_display = ("account", "currency")


class OperationAdmin(admin.ModelAdmin):
    list_display = (
        "purpose_of_payment",
        "summ",
        "from_account",
        "to_account",
        "time_operation",
    )


admin.site.register(Fund, FundAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Operation, OperationAdmin)
