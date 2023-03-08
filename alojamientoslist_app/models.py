from django.db import models

# Create your models here.
class Alojamiento(models.Model):
    nombre_alojamiento = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_alojamiento