from django.urls import path
from alojamientoslist_app.api.views import alojamiento_list, alojamiento_detail

urlpatterns = [
    path('list/', alojamiento_list, name='alojamiento-listar'),
    path('<int:indice>', alojamiento_detail, name='alojamiento-detalle')
]