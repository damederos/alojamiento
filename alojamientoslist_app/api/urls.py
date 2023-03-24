from django.urls import path
from alojamientoslist_app.api.views import alojamiento_list, alojamiento_detail, periodo_list, periodo_detail

urlpatterns = [
    #rutas de alojamientos
    path('alojamientos/', alojamiento_list, name='alojamiento-listar'),
    path('alojamientos/<int:indice>', alojamiento_detail, name='alojamiento-detalle'),
    #rutas de periodo vacacionales
    path('periodos/', periodo_list, name='periodo-listar'),
    path('periodos/<int:indice>', periodo_detail, name='periodo-detalle')
]