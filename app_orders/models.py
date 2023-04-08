from django.db import models
from django.urls import reverse

from app_category.models import Activity, Categoryes, Specialization
from app_users.models import CustomUser

class Order(models.Model):
    name = models.CharField(max_length=150, default='')
    description = models.TextField()
    price = models.IntegerField(default=1000)
    slug = models.SlugField(max_length=100, unique=True, default='')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    category = models.ForeignKey(Categoryes, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse ('orders', kwargs={'order_id': self.slug})


