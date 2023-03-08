from django.urls import path
from alojamientoslist_app.views import alojamiento_list

urlpatterns = [
    path('list/', alojamiento_list, name='alojamiento-list')
]