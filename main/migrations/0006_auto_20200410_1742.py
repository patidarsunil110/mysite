# Generated by Django 3.0.2 on 2020-04-10 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200407_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='is_session_active',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
