from django.urls import path
from alojamientoslist_app.api.views import (PersonaList, PersonaDetail, CargoList, CargoDetail)

urlpatterns = [
    #Personas
    #registro de cliente
    path('registro-cliente/', PersonaList.as_view(http_method_names=['post']), name='persona-register'),
    #listar cliente
    path('clientes/', PersonaList.as_view(http_method_names=['get']), name='persona-list'),
    #buscar cliente x id
    path('cliente/<uuid:pk>', PersonaDetail.as_view(), name='persona-detail'),


    #gestion de cargo
    path('cargo/', CargoList.as_view(), name='cargo-list'),
    path('cargo/<int:pk>', CargoDetail.as_view(), name='cargo-detail'),
]
