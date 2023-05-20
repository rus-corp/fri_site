# Generated by Django 4.1.6 on 2023-05-17 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='account',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='currency',
        ),
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(choices=[('RUB', 'Рубли'), ('USD', 'Доллары США')], default='RUB', max_length=3, verbose_name='валюта счета'),
        ),
        migrations.AddField(
            model_name='fund',
            name='rub_account',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rub_fund', to='app_accounts.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fund',
            name='usd_account',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='usd_fund', to='app_accounts.account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operation',
            name='summ',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма'),
        ),
    ]