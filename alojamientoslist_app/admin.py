from django.contrib import admin
from alojamientoslist_app.models import Alojamiento, Provincia, Periodo_vacacional

# Register your models here.
admin.site.register(Alojamiento)
admin.site.register(Provincia)
admin.site.register(Periodo_vacacional)
