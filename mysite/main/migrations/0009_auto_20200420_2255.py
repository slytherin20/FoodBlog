# Generated by Django 2.2.12 on 2020-04-20 22:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200420_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='receipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmark', to='main.Receipe'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 22, 55, 10, 949946)),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='bookmarked_receipe',
            field=models.ManyToManyField(related_name='receipe', through='main.Bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 22, 55, 10, 948340), verbose_name='Date Published'),
        ),
    ]
