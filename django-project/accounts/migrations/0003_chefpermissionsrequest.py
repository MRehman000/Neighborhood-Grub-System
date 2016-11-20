# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 03:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_terminateaccountrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefPermissionsRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_dish_name', models.CharField(max_length=256)),
                ('first_dish_image', models.ImageField(max_length=256, upload_to='')),
                ('second_dish_name', models.CharField(max_length=256)),
                ('second_dish_image', models.ImageField(max_length=256, upload_to='')),
                ('third_dish_name', models.CharField(max_length=256)),
                ('third_dish_image', models.ImageField(max_length=256, upload_to='')),
                ('video_biography', models.FileField(max_length=256, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]