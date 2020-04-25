# Generated by Django 2.2.12 on 2020-04-20 08:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20200420_0601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='bookmarked_receipe',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 8, 23, 49, 943160)),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 8, 23, 49, 942488), verbose_name='Date Published'),
        ),
        migrations.CreateModel(
            name='bookmarkedreceipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Receipe')),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark_or_not', models.BooleanField(default=True)),
                ('bookmarked_receipe', models.ManyToManyField(to='main.bookmarkedreceipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]