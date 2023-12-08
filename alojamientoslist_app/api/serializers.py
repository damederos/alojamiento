from rest_framework import serializers
from alojamientoslist_app.models import (Periodo_vacacional, Persona, Alojamiento, Cargo, Reservacion)

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

    def validated_nombre_completo(self, data):
        if len(data)<3:
            raise serializers.ValidationError("El nombre del huesped es muy corto")
        else:
            return data

class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = ['id_reservacion', 'fecha_inicio', 'fecha_fin', 'fecha_registro', 'cancelada']

class PeriodoSerializer(serializers.ModelSerializer):
    reservacionlist = ReservacionSerializer(many=True, read_only=True)
    class Meta:
        model = Periodo_vacacional
        exclude = ['id_periodo']

    def validate(self, data):
        if data['fecha_inicio'] >= data['fecha_fin']:
            raise serializers.ValidationError("La fecha de inicio no puede ser mayor que la fecha final")
        else:
            return data

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'