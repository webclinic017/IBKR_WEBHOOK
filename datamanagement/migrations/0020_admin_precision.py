# Generated by Django 4.2.7 on 2023-11-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanagement', '0019_alter_admin_oanda_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='precision',
            field=models.FloatField(default=1),
        ),
    ]
