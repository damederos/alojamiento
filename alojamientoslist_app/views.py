# from django.shortcuts import render
# from alojamientoslist_app.models import Alojamiento
# from django.http import JsonResponse

# # Create your views here.
# def alojamiento_list(request):
#     alojamientos = Alojamiento.objects.all()
#     # Creando un diccionario tipo data
#     data = {
#         'alojamientos': list(alojamientos.values())
#     }
#     return JsonResponse(data)

# def alojamiento_detail(request, indice):
#     alojamientos = Alojamiento.objects.get(pk=indice)
#     data = {
#         'nombre_alojamiento': alojamientos.nombre_alojamiento,
#         'capacidad': alojamientos.capacidad,
#         'activo': alojamientos.activo
#     }
#     return JsonResponse(data)

    