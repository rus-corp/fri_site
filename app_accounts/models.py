from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    CURRENCY_CHOICES = (
        ("RUB", _("Рубли")),
        ("USD", _("Доллары США")),
    )
    currency = models.CharField(
        _("валюта счета"), max_length=3, choices=CURRENCY_CHOICES, default="RUB"
    )
    account = models.CharField(_("Cчёт"), max_length=55, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.account

    class Meta:
        verbose_name = _("счёт")
        verbose_name_plural = _("счета")


class Operation(models.Model):
    # CURRENCY_CHOICES = (
    #     ("RUB", _("Рубли")),
    #     ("USD", _("Доллары США")),
    # )
    # currency = models.CharField(
    #     _("валюта операции"), max_length=3, choices=CURRENCY_CHOICES, default="RUB"
    # )
    purpose_of_payment = models.CharField(_("назначение платежа"), max_length=255)
    summ = models.DecimalField(_("сумма"), max_digits=10, decimal_places=2)
    from_account = models.ForeignKey(
        Account,
        related_name="f_acc",
        on_delete=models.PROTECT,
        verbose_name=_("счёт списания"),
    )
    to_account = models.ForeignKey(
        Account,
        related_name="t_acc",
        on_delete=models.PROTECT,
        verbose_name=_("счёт зачисления"),
    )
    time_operation = models.DateTimeField(_("время проводки"), auto_now_add=True)

    class Meta:
        ordering = ("-time_operation",)
        verbose_name = _("транзакция")
        verbose_name_plural = _("транзакции")


class Fund(models.Model):
    name = models.CharField(_("наименование фонда"), max_length=255, unique=True)
    rub_account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="rub_fund"
    )
    usd_account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="usd_fund"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("фонд")
        verbose_name_plural = _("фонды")

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         count = Account.objects.count()
    #         self.rub_acc = Account.objects.create(account=f"{date.today().strftime('%y%m%d')}{count+1}")
    #         self.usd_acc = Account.objects.create(account=f"{date.today().strftime('%y%m%d')}{count+2}", currency="USD")
    #     super().save(*args, **kwargs)
