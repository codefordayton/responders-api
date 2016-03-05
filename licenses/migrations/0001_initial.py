# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-05 16:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_class', models.TextField(choices=[('DOC', 'Physician'), ('NURSE', 'Nurse'), ('EMT', 'EMT')])),
                ('license_name', models.TextField(blank=True, null=True)),
                ('license_number', models.TextField()),
                ('initial_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('zip_code', models.TextField()),
                ('record_created', models.DateField(auto_now_add=True)),
                ('record_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='license',
            name='specialties',
            field=models.ManyToManyField(to='licenses.Specialty'),
        ),
        migrations.AddField(
            model_name='license',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
