# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-01 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20171001_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Signup', to_field=b'email'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
