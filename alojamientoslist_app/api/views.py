
from alojamientoslist_app.api.serializers import (PersonaSerializer, CargoSerializer, AlojamientoSerializer, PeriodoSerializer,
                                                  ReservacionSerializer)
from alojamientoslist_app.models import (Persona, Cargo, Alojamiento, Periodo_vacacional, Reservacion)
from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from alojamientoslist_app.api.permissions import AdminOrReadOnly
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
class CargoVS(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

#crud de alojamiento
class AlojamientoVS(viewsets.ModelViewSet):
    queryset = Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer

#crud de periodo vacacional
class PeriodoVS(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Periodo_vacacional.objects.all()
    serializer_class = PeriodoSerializer

class PeriodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Periodo_vacacional.objects.all()
    serializer_class = PeriodoSerializer

class ReservacionCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReservacionSerializer

    def get_queryset(self):
        return Reservacion.objects.all()

    def perform_create(self, serializer):
        #esto trae el id en la url
        pk = self.kwargs.get('pk')
        vacaciones = Periodo_vacacional.objects.get(pk=pk)
        user = self.request.user
        reservacion_queryset = Reservacion.objects.filter(id_periodo=vacaciones, id_usuario=user)
        if reservacion_queryset.exists():
            raise ValidationError("El ususario ya registro su reservacion en este periodo vacacional")
        serializer.save(id_periodo=vacaciones, id_usuario=user)

class ReservacionList(generics.ListAPIView):
    serializer_class = ReservacionSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reservacion.objects.filter(id_periodo=pk)

class ReservacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer