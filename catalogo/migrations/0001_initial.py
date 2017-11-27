# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 20:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('nroDoc', models.CharField(max_length=8)),
                ('total', models.FloatField(default=0)),
                ('direccion', models.CharField(max_length=100)),
                ('nroBoleta', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Alquiler',
                'verbose_name_plural': 'Alquileres',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(blank=True, max_length=10)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Persona')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name': 'Comprobante',
                'verbose_name_plural': 'Comprobantes',
            },
        ),
        migrations.CreateModel(
            name='DetalleAlquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(default=0)),
                ('cantidad', models.FloatField(default=0)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('importe', models.FloatField(default=0)),
                ('alquiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Alquiler')),
            ],
            options={
                'verbose_name': 'DetalleAlquiler',
                'verbose_name_plural': 'DetalleAlquileres',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('nro_oficina', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.BooleanField(default=False)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Categoria')),
            ],
            options={
                'verbose_name': 'Oficina',
                'verbose_name_plural': 'Oficinas',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroReserva', models.CharField(max_length=10)),
                ('fechaFin', models.DateField(blank=True, null=True)),
                ('fechaReserva', models.DateField(blank=True, null=True)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Persona')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='TipoTrabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'TipoTrabajador',
                'verbose_name_plural': 'TipoTrabajadores',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.TipoTrabajador')),
                ('trabajador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
        migrations.AddField(
            model_name='reserva',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Trabajador'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='oficina',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Oficina'),
        ),
        migrations.AddField(
            model_name='detallealquiler',
            name='descripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Oficina'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Cliente'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='comprobante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Comprobante'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Trabajador'),
        ),
    ]
