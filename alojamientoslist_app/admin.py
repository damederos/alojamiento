from django.contrib import admin
from alojamientoslist_app.models import (Provincia, Periodo_vacacional, Persona, Municipio,
                                         Alojamiento, Cargo, Reservacion)

admin.site.register(Provincia)
admin.site.register(Periodo_vacacional)
admin.site.register(Municipio)
admin.site.register(Alojamiento)
admin.site.register(Cargo)
admin.site.register(Reservacion)