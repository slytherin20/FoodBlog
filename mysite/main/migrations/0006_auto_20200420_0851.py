# Generated by Django 2.2.12 on 2020-04-20 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200420_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 8, 51, 30, 255388)),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 8, 51, 30, 254720), verbose_name='Date Published'),
        ),
    ]
