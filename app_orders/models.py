from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from app_category.models import Activity, Categoryes, Specialization
from app_users.models import CustomUser

class Order(models.Model):
    ORDER_TYPES = [
        ('1', _('Предварительный')),
        ('2', _('Опубликованный')),
        ('3', _('Принятый')),
        ('4', _('Выполненный')),
    ]
    name = models.CharField(max_length=150, default='')
    description = models.TextField()
    price = models.IntegerField(default=1000)
    slug = models.SlugField(max_length=100, unique=True, default='')

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    category = models.ForeignKey(Categoryes, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    #активность заказа
    status = models.CharField(_('статус заказа'), choices=ORDER_TYPES, default='1', max_length=1)
    #заказчик
    customer = models.ForeignKey(CustomUser, on_delete=models.PROTECT)


    def __str__(self) -> str:
        return f'{self.name}, {self.description}, {self.price} '
    
    def get_absolute_url(self):
        return reverse ('orders', kwargs={'order_id': self.slug})


class OrderExecCust(models.Model):
    STATUS_CHOICE = [
        ('1', _('Кандидат')),
        ('2', _('Исполнитель')),
    ]
    order = models.ForeignKey(Order, related_name='orders')
    #исполнитель
    executor = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='executors')
    executor_status = models.CharField(_('статус исполнителя'), choices=STATUS_CHOICE, max_length=1)


class OrderChat(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    description = models.TextField(max_length=1000)
