# Generated by Django 4.1.6 on 2023-04-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_referral_link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get_referral',
            name='file1',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
