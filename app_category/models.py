from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=150, )

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'

    def __str__(self) -> str:
        return self.name
    

class Categoryes(models.Model):
    name = models.CharField(max_length=200)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='category')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name
    

class Specialization(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categoryes, on_delete=models.CASCADE, related_name='specialization')

    class Meta:
        verbose_name = 'Специализации'
        verbose_name_plural = 'Специализации'
        

    def __str__(self) -> str:
        return self.name