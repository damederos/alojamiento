from rest_framework import serializers

class AlojamientoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre_alojamiento = serializers.CharField()
    capacidad = serializers.CharField()
    activo = serializers.BooleanField()

class Periodo_vacacionalSerializer(serializers.Serializer):
    id_periodo = serializers.IntegerField(read_only=True)
    nombre_periodo = serializers.CharField()
    fecha_inicio = serializers.DateField()
    fecha_fin = serializers.DateField()
    activo = serializers.BooleanField()