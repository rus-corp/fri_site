
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0001_initial'),
        ('app_users', '0002_customuser_on_vacation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='acc',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_accounts.account'),
        ),
    ]
