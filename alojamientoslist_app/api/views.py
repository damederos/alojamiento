from alojamientoslist_app.models import Alojamiento, Periodo_vacacional
from alojamientoslist_app.api.serializers import AlojamientoSerializer, Periodo_vacacionalSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#crud de alojamientos
@api_view()
def alojamiento_list(request):
    alojamientos = Alojamiento.objects.all()
    serializer = AlojamientoSerializer(alojamientos, many=True)
    return Response(serializer.data)

@api_view()
def alojamiento_detail(request, indice):
    alojamientos = Alojamiento.objects.get(pk=indice)
    serializer = AlojamientoSerializer(alojamientos)
    return Response(serializer.data)

#crud de periodos vacacionales
@api_view()
def periodo_list(request):
    periodo = Periodo_vacacional.objects.all()
    serializer = Periodo_vacacionalSerializer(periodo, many=True)
    return Response(serializer.data)

@api_view()
def periodo_detail(request, indice):
    periodo = Periodo_vacacional.objects.get(pk=indice)
    serializer = Periodo_vacacionalSerializer(periodo)
    return Response(serializer.data)