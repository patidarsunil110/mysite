# Generated by Django 3.0.2 on 2020-04-11 13:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('main', '0008_auto_20200410_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 19, 21, 53, 961584), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='session_key',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='sessions.Session'),
        ),
    ]