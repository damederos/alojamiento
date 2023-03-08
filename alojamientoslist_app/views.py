from django.shortcuts import render
from alojamientoslist_app.models import Alojamiento
from django.http import JsonResponse

# Create your views here.
def alojamiento_list(request):
    alojamientos = Alojamiento.objects.all()
    # Creando un diccionario tipo data
    data = {
        'alojamientos': list(alojamientos.values())
    }
    return JsonResponse(data)