from django.db import models


from app_users.models import CustomUser

class Order(models.Model):
    description = models.TextField()
    price = models.IntegerField(default=1000)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name

