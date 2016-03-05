# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-05 17:43
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('licenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.TextField()),
                ('phone', models.TextField(blank=True, null=True)),
                ('twitter', models.TextField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='license',
            name='zip_code',
        ),
    ]