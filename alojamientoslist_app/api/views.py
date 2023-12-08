
from alojamientoslist_app.api.serializers import (PersonaSerializer, CargoSerializer, AlojamientoSerializer, PeriodoSerializer,
                                                  ReservacionSerializer)
from alojamientoslist_app.models import (Persona, Cargo, Alojamiento, Periodo_vacacional, Reservacion)
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#crud de Persona
class PersonaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PersonaDetail(mixins.RetrieveModelMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#crud de cargo
class CargoList(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class CargoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

#crud de alojamiento
class AlojamientoList(generics.ListCreateAPIView):
    queryset = Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer

class AlojamientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer

#crud de periodo vacacional
class PeriodoList(generics.ListCreateAPIView):
    queryset = Periodo_vacacional.objects.all()
    serializer_class = PeriodoSerializer

class PeriodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Periodo_vacacional.objects.all()
    serializer_class = PeriodoSerializer

class ReservacionCreate(generics.CreateAPIView):
    serializer_class = ReservacionSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        vacaciones = Periodo_vacacional.objects.get(pk=pk)
        serializer.save(id_periodo=vacaciones)

class ReservacionList(generics.ListAPIView):
    serializer_class = ReservacionSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reservacion.objects.filter(id_periodo=pk)

class ReservacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer


