from rest_framework import serializers
from alojamientoslist_app.models import (Periodo_vacacional, Alojamiento, Cargo, Reservacion)


class ReservacionSerializer(serializers.ModelSerializer):
    id_usuario = serializers.StringRelatedField(read_only=True)
    #nombre_usuario = serializers.CharField(source='Perosona.username')
    class Meta:
        model = Reservacion
        exclude = ['id_periodo']

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

class AlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = '__all__'

