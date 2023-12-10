from django.urls import path, include
from rest_framework.routers import DefaultRouter
from alojamientoslist_app.api.views import (PersonaList, PersonaDetail, CargoVS, AlojamientoVS,
                                            PeriodoVS, ReservacionCreate, ReservacionList, ReservacionDetail)
router = DefaultRouter()
router.register('cargo', CargoVS, basename='cargo')
router.register('alojamiento', AlojamientoVS, basename='alojamiento')
router.register('periodo', PeriodoVS, basename='periodo')

urlpatterns = [
    #Personas
    #registro de cliente
    path('registro-cliente/', PersonaList.as_view(http_method_names=['post']), name='persona-register'),
    #listar cliente
    path('clientes/', PersonaList.as_view(http_method_names=['get']), name='persona-list'),
    #buscar cliente x id
    path('cliente/<uuid:pk>', PersonaDetail.as_view(), name='persona-detail'),

    #gestion de cargo, periodo y alojamiento
    path('', include(router.urls)),

    #Gestionar reservacion
    #crear reservacion
    path('periodo/<int:pk>/reservation-create/', ReservacionCreate.as_view(), name='reservacion-create'),
    path('periodo/<int:pk>/reservations/', ReservacionList.as_view(), name='reservacion-list'),
    path(' <int:pk>/', ReservacionDetail.as_view(), name='reservacion-detail')
]
