# Generated by Django 5.0 on 2024-01-04 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='bank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_accounts', to='accounts.bank'),
        ),
    ]
