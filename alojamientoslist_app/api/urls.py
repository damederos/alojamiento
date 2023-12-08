from django.urls import path
from alojamientoslist_app.api.views import (PersonaList, PersonaDetail, CargoList, CargoDetail, AlojamientoList, AlojamientoDetail,
                                            PeriodoList, PeriodoDetail, ReservacionCreate, ReservacionList, ReservacionDetail)

urlpatterns = [
    #Personas
    #registro de cliente
    path('registro-cliente/', PersonaList.as_view(http_method_names=['post']), name='persona-register'),
    #listar cliente
    path('clientes/', PersonaList.as_view(http_method_names=['get']), name='persona-list'),
    #buscar cliente x id
    path('cliente/<uuid:pk>', PersonaDetail.as_view(), name='persona-detail'),

    #gestion de cargo
    path('cargos/', CargoList.as_view(), name='cargo-list'),
    path('cargo/<int:pk>', CargoDetail.as_view(), name='cargo-detail'),

    #gestion de alojamiento
    path('alojamientos/', AlojamientoList.as_view(), name='alojamiento-list'),
    path('alojamiento/<int:pk>', AlojamientoDetail.as_view(), name='alojamiento-detail'),

    #gestion de periodo Vacacional
    path('periodos/', PeriodoList.as_view(), name='periodo-list'),
    path('periodo-vacacional/<int:pk>', PeriodoDetail.as_view(), name='periodo-detail'),

    #Gestionar reservacion
    #crear reservacion
    path('periodo/<int:pk>/reservation-create/', ReservacionCreate.as_view(), name='reservacion-create'),
    path('periodo/<int:pk>/reservations/', ReservacionList.as_view(), name='reservacion-list'),
    path('periodo/reservation/<int:pk>/', ReservacionDetail.as_view(), name='reservacion-detail')
]
