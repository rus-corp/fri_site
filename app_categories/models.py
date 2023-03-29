from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


# Create your models here.

class Specializtion(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='специализации')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Специализация')
    slug = models.SlugField(max_length=150)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Специализация'
        verbose_name_plural= 'Специализации'


    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse ('specializations', args=[str(self.slug)])

class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Категории')
    specialization = TreeForeignKey(Specializtion, on_delete=models.PROTECT, related_name='specializations', verbose_name='Категории')
    slug = models.SlugField(max_length=150)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'  
        verbose_name_plural = 'Категории'
        
