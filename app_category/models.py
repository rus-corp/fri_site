from django.db import models
from django.urls import reverse
from transliterate import translit
from django.utils.text import slugify




# from app_users.models import CustomUser
# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=150, )
    slug = models.SlugField(max_length=55, unique=True, default='')

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'

    def __str__(self) -> str:
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('categoryes', kwargs={'activity_slug': self.slug})
    
    def save(self, *args, **kwargs):
        try:
            name = translit(self.name, reversed=True)
            self.slug = slugify(name)
        except:
            self.slug = slugify(self.name)
        super(Activity, self).save(*args, **kwargs)




class Categoryes(models.Model):
    name = models.CharField(max_length=200)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='categoryes')
    slug = models.SlugField(max_length=55, unique=True, default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


    def save(self, *args, **kwargs):
        try:
            name = translit(self.name, reversed=True)
            self.slug = slugify(name)
        except:
            self.slug = slugify(self.name)
        super(Categoryes, self).save(*args, **kwargs)
    

class Specialization(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categoryes, on_delete=models.CASCADE, related_name='specializations')
    slug = models.SlugField(max_length=155, unique=True, default='')


    class Meta:
        verbose_name = 'Специализации'
        verbose_name_plural = 'Специализации'
        

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        try:
            name = translit(self.name, reversed=True)
            self.slug = slugify(name)
        except:
            self.slug = slugify(self.name)
        super(Specialization, self).save(*args, **kwargs)
    

class SpecializationUser(models.Model):
    users = models.ForeignKey(to='app_users.CustomUser', on_delete=models.CASCADE, related_name='users')
    specializations = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='specializations')


