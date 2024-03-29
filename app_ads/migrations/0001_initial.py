# Generated by Django 4.1.6 on 2023-04-23 21:50

import app_ads.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='заголовок')),
                ('description', models.TextField(blank=True, db_index=True, verbose_name='описание')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=10, verbose_name='цена')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='дата обновления')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url-адрес')),
                ('image', models.ImageField(blank=True, db_index=True, upload_to='category/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'svg'], message='Ошибка загрузки: допускаются только файлы с расширением .jpg .gif .png .svg'), app_ads.validators.image_size_validate], verbose_name='изображение')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='app_ads.category', verbose_name='родительская категория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
    ]
