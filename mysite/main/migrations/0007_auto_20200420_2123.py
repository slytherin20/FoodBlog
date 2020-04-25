# Generated by Django 2.2.12 on 2020-04-20 21:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20200420_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='title',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='receipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Receipe'),
        ),
        migrations.AddField(
            model_name='receipe',
            name='bookmarked_receipe',
            field=models.ManyToManyField(through='main.Bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 21, 23, 45, 695708)),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 21, 23, 45, 694180), verbose_name='Date Published'),
        ),
        migrations.DeleteModel(
            name='bookmarkedreceipe',
        ),
    ]