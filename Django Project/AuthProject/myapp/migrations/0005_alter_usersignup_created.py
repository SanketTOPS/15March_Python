# Generated by Django 4.2.1 on 2023-06-24 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 11, 49, 50, 641164)),
        ),
    ]