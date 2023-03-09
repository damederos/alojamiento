from django.db import models

# Create your models here.
class Alojamiento(models.Model):
    nombre_alojamiento = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_alojamiento

class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_provincia

class Periodo_vacacional(models.Model):
    id_periodo = models.BigAutoField(primary_key=True)
    nombre_periodo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_periodo
