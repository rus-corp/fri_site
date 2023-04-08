# Generated by Django 4.1.6 on 2023-04-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='slug',
            field=models.SlugField(default='', max_length=55, unique=True),
        ),
        migrations.AddField(
            model_name='categoryes',
            name='slug',
            field=models.SlugField(default='', max_length=55, unique=True),
        ),
        migrations.AddField(
            model_name='specialization',
            name='slug',
            field=models.SlugField(default='', max_length=55, unique=True),
        ),
        migrations.AlterField(
            model_name='categoryes',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryes', to='app_category.activity'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specializations', to='app_category.categoryes'),
        ),
    ]