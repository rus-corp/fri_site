# Generated by Django 4.1.6 on 2023-04-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0002_rename_user_order_customer_order_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=models.SlugField(max_length=80, unique=True),
        ),
    ]
