# Generated by Django 5.2.3 on 2025-06-24 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0002_barrio_numero_edificios_residenciales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrio',
            name='numero_edificios_residenciales',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='barrio',
            name='numero_parques',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')]),
        ),
        migrations.AlterField(
            model_name='barrio',
            name='numero_viviendas',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='barrio',
            name='parroquia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrios', to='ordenamiento.parroquia'),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='tipo',
            field=models.CharField(choices=[('Urbana', 'Urbana'), ('Rural', 'Rural')], max_length=10),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='ubicacion',
            field=models.CharField(choices=[('Norte', 'Norte'), ('Sur', 'Sur'), ('Este', 'Este'), ('Oeste', 'Oeste')], max_length=10),
        ),
    ]
