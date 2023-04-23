from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from DjBusinessPlatform.settings import SHARES
# from app_personal_account.models import Transaction
from .models import CustomUser
from app_accounts.models import Operation, Fund


# class TransactionInline(admin.TabularInline):
#     model = Transaction
#     readonly_fields = ['datetime', 'balance_before', 'balance_after', 'exist']
#     fk_name = 'user'


class CustomUserAdmin(admin.ModelAdmin):
    # чтобы в админке отобразить древовидную структуру, нужно унаследовать от DjangoMpttAdmin
    list_display = (
        'id', 'email', 'email_confirmed', 'get_personal_account', 'last_name', 'first_name', 'get_referer', 'status',
        'is_core', 'on_vacation', 'balance', 'date_joined')
    list_filter = (
        'date_joined', 'is_staff', 'is_active', 'on_vacation', 'email_confirmed', 'is_core', 'status',
        'paid_entrance_fee')
    search_fields = (
        'id', 'email', 'last_name', 'first_name', 'patronymic', 'parent__last_name', 'parent__email', 'personal_number')
    readonly_fields = ['date_joined', 'get_referrals', 'referral_url', 'parent', 'balance', 'get_personal_account']
    save_on_top = True
    actions = ['make_active', 'make_inactive', 'paid_entrance_fee', 'deposit_fee']

    # inlines = [TransactionInline]
    def deposit_fee(self, request, queryset):
        pass
    deposit_fee.short_description = _('Оплата депозита')

    def paid_entrance_fee(self, request, queryset):
        queryset.update(paid_entrance_fee=True)
        for r_user in queryset:
            Operation.objects.create(purpose_of_payment='оплата вступления', summ=2000,
                                     from_account=Fund.objects.get(name='Вступительные взносы').account,
                                     to_account=r_user.acc)
            Operation.objects.create(purpose_of_payment='вступительный взнос', summ=1999, from_account=r_user.acc,
                                     to_account=Fund.objects.get(name='Вступительный фонд').account)
            Operation.objects.create(purpose_of_payment='паевой взнос', summ=1, from_account=r_user.acc,
                                     to_account=Fund.objects.get(name='Паевой фонд').account)
            Operation.objects.create(purpose_of_payment='на развитие', summ=999,
                                     from_account=Fund.objects.get(name='Вступительный фонд').account,
                                     to_account=Fund.objects.get(name='Фонд развития').account)
            Operation.objects.create(purpose_of_payment='на потребление', summ=1000,
                                     from_account=Fund.objects.get(name='Вступительный фонд').account,
                                     to_account=Fund.objects.get(name='Фонд потребления').account)
            for i, sum_ref in enumerate(SHARES):
                if r_user.parent:
                    r_user = r_user.parent
                    Operation.objects.create(purpose_of_payment='бонус', summ=sum_ref,
                                             from_account=Fund.objects.get(name='Фонд потребления').account,
                                             to_account=r_user.acc)
                else:
                    Operation.objects.create(purpose_of_payment='невостребованный бонус', summ=sum(SHARES[i:]),
                                             from_account=Fund.objects.get(name='Фонд потребления').account,
                                             to_account=Fund.objects.get(name='Невостребованные бонусы').account)
                    break
    paid_entrance_fee.short_description = _('Оплатил вступительный взнос')

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = _('активировать')

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = _('деактивировать')

    def referral_url(self, obj):
        return obj.get_referral_url()

    referral_url.short_description = _('ссылка-приглашение')

    def get_referrals(self, obj):
        referrals = obj.referrals
        return f"1 level: {referrals.get('level1').count()}\n" \
               f"2 level: {referrals.get('level2').count()}\n" \
               f"3 level: {referrals.get('level3').count()}"

    get_referrals.short_description = _('рефералы')

    def get_referer(self, obj):
        link = reverse("admin:app_users_customuser_change", args=[obj.parent_id])
        return format_html('<a href="{}">{}</a>', link, obj.parent)

    get_referer.short_description = _('реферер')

    def get_personal_account(self, obj):
        return obj.personal_account

    get_personal_account.short_description = _('лицевой счет')


admin.site.register(CustomUser, CustomUserAdmin)
