from django.db import models

class Parroquia(models.Model):
    UBICACION_CHOICES = [
        ('Norte', 'Norte'),
        ('Sur', 'Sur'),
        ('Este', 'Este'),
        ('Oeste', 'Oeste'),
    ]

    TIPO_CHOICES = [
        ('Urbana', 'Urbana'),
        ('Rural', 'Rural'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=10, choices=UBICACION_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre


class Barrio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    numero_viviendas = models.PositiveIntegerField()
    numero_parques = models.IntegerField(choices=[(i, str(i)) for i in range(1, 7)])
    numero_edificios_residenciales = models.PositiveIntegerField(default=0)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return self.nombre
