# Generated by Django 4.1.6 on 2023-04-23 21:50

import app_users.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email')),
                ('email_confirmed', models.BooleanField(default=False, verbose_name='email подтвержден')),
                ('slug', models.SlugField(max_length=55, unique=True, verbose_name='имя пользователя')),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=55, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=55, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, db_index=True, max_length=55, verbose_name='Отчество')),
                ('country', models.CharField(blank=True, db_index=True, max_length=55, verbose_name='Страна')),
                ('address', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Адрес')),
                ('personal_number', models.CharField(blank=True, db_index=True, max_length=17, null=True, verbose_name='ИНН или персональный номер')),
                ('document', models.FileField(blank=True, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'pdf'], message='Ошибка загрузки: допускаются только файлы с расширением .jpg .pdf .png'), app_users.validators.document_size_validate], verbose_name='документ')),
                ('document_number', models.CharField(blank=True, db_index=True, max_length=55, verbose_name='Серия и номер документа')),
                ('document_issued', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Когда и кем выдан')),
                ('paid_entrance_fee', models.BooleanField(default=False, verbose_name='Оплатил вступительный взнос')),
                ('status', models.CharField(choices=[('0', 'Участник Заказчик'), ('1', 'Кандидат'), ('2', 'Участник Фрилансер')], db_index=True, default='0', max_length=30, verbose_name='статус')),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата регистрации')),
                ('is_active', models.BooleanField(default=True, verbose_name='является активным')),
                ('is_staff', models.BooleanField(default=False, verbose_name='является сотрудником')),
                ('is_core', models.BooleanField(db_index=True, default=False, verbose_name='основатель')),
                ('on_vacation', models.BooleanField(db_index=True, default=False, verbose_name='в отпуске')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'], message='Ошибка загрузки: допускаются только файлы с расширением .jpg .gif .png'), app_users.validators.avatar_size_validate])),
                ('phone_number', models.CharField(blank=True, db_index=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+79012345678'.", regex='^\\+\\d{11,15}')], verbose_name='номер телефона')),
                ('balance', models.DecimalField(db_index=True, decimal_places=2, default=0, max_digits=10, verbose_name='баланс')),
                ('bank_name', models.CharField(blank=True, max_length=255, verbose_name='Наименование банка')),
                ('bank_address', models.CharField(blank=True, max_length=255, verbose_name='Адрес банка')),
                ('bank_bic', models.CharField(blank=True, max_length=55, null=True, verbose_name='БИК банка')),
                ('bank_correspondent_account', models.CharField(blank=True, max_length=55, null=True, verbose_name='Корреспондентский счет банка')),
                ('payment_account', models.CharField(blank=True, max_length=55, null=True, verbose_name='Расчетный счет')),
                ('recipients_name', models.CharField(blank=True, max_length=255, verbose_name='Имя получателя платежа')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('acc', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_accounts.account')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to=settings.AUTH_USER_MODEL, verbose_name='родитель')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]
