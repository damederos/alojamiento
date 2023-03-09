from alojamientoslist_app.models import Alojamiento
from alojamientoslist_app.api.serializers import AlojamientoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

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