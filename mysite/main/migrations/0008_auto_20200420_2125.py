# Generated by Django 2.2.12 on 2020-04-20 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200420_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 21, 25, 37, 287233)),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 21, 25, 37, 285709), verbose_name='Date Published'),
        ),
    ]