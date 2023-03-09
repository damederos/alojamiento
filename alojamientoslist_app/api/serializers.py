from rest_framework import serializers

class AlojamientoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre_alojamiento = serializers.CharField()
    capacidad = serializers.CharField()
    activo = serializers.BooleanField()