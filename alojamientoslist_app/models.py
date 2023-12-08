from django.db import models
import uuid

# Create your models here.
class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=150, null=False, blank=False)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return self.nombre_cargo

class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100, null=False, blank=False)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return self.nombre_provincia

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre_municipio = models.CharField(max_length=100, null=False, blank=False)
    activo = models.BooleanField(default=True, blank=False, null=False)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, verbose_name="provincias", related_name="municipio")

    def __str__(self):
        return self.nombre_municipio

class Alojamiento(models.Model):
    id_alojamiento = models.AutoField(primary_key=True)
    nombre_alojamiento = models.CharField(max_length=200, null=False, blank=False)
    capacidad = models.IntegerField(null=False)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return self.nombre_alojamiento

class Periodo_vacacional(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    nombre_periodo = models.CharField(max_length=250, null=False, blank=False)
    fecha_inicio = models.DateTimeField(blank=False, null=False)
    fecha_fin = models.DateTimeField(blank=False, null=False)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return self.nombre_periodo

class Persona(models.Model):
    id_persona = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_completo = models.CharField(max_length=150, null=False, blank=False)
    ci = models.CharField(max_length=32, null=False, blank=False)
    class Genero(models.TextChoices):
        FEMENINO = "F", "Femenino"
        MASCULINO = "M", "Masculino"
    sexo = models.CharField(max_length=1, choices=Genero.choices, default=Genero.FEMENINO, blank=False, null=False)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, verbose_name="cargos", related_name="personacargo")
    id_municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name="municipios", related_name="personamunicipio")
    correo = models.EmailField(max_length=254, unique=True, null=True)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return self.nombre_completo

class Reservacion(models.Model):
    id_reservacion = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=False, blank=False, related_name="personareserva", verbose_name="personas")
    id_periodo = models.ForeignKey(Periodo_vacacional, on_delete=models.PROTECT, related_name="reservacionlist", verbose_name="periodos")
    id_alojamiento = models.ForeignKey(Alojamiento, on_delete=models.PROTECT, related_name="reservalojamiento", verbose_name="alojamientos")
    fecha_inicio = models.DateTimeField(blank=False, null=False)
    fecha_fin = models.DateTimeField(blank=False, null=False)
    fecha_registro = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    cancelada = models.BooleanField(default=False, blank=False, null=False)

    def __int__(self):
        return self.id_reservacion

