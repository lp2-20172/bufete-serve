# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallealquiler',
            name='descripcion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Oficina'),
        ),
    ]
