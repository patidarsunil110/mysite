# Generated by Django 3.0.2 on 2020-04-11 14:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sessions', '0001_initial'),
        ('main', '0009_auto_20200411_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 19, 41, 10, 579784), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='session_key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
