
from alojamientoslist_app.api.serializers import (CargoSerializer, AlojamientoSerializer, PeriodoSerializer,
                                                  ReservacionSerializer)
from alojamientoslist_app.models import (Persona, Cargo, Alojamiento, Periodo_vacacional, Reservacion)
from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from alojamientoslist_app.api.permissions import (AdminOrReadOnly, ReservacionUser, IsAdminStaff)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from alojamientoslist_app.api.throttling import ReservacionCreateThrottle

#crud de Persona
#class PersonaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#    queryset = Persona.objects.all()
    #serializer_class = PersonaSerializer

#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)

#    def post(self, request, *args, **kwargs):
 #       return self.create(request, *args, **kwargs)

#class PersonaDetail(mixins.RetrieveModelMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#    queryset = Persona.objects.all()
#    serializer_class = PersonaSerializer

#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)

#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)

#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)

#crud de cargo
class CargoVS(viewsets.ModelViewSet):
    #permission_classes = [IsAdminStaff]
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

#crud de alojamiento
class AlojamientoVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminStaff]
    queryset = Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer

#crud de periodo vacacional
class PeriodoVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminStaff]
    queryset = Periodo_vacacional.objects.all()
    serializer_class = PeriodoSerializer

class PeriodoList(generics.ListAPIView):
   serializer_class = PeriodoSerializer

   def get_queryset(self):
       return Periodo_vacacional.objects.filter(activo=True)




class ReservacionCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ReservacionUser]
    serializer_class = ReservacionSerializer
    throttle_classes = [ReservacionCreateThrottle]

    def get_queryset(self):
        username = self.request.query_params('username', None)
        return Reservacion.objects.filter(id_usuario__usuario=username)

    def perform_create(self, serializer):
        #esto trae el id del periodo vacacional en la url
        pk = self.kwargs.get('pk')
        #obtiene el periodo segun su id
        vacaciones = Periodo_vacacional.objects.get(pk=pk)
        #datos de user autenticado
        #user = self.request.user
        #reservacion_usuario = Reservacion.objects.filter(id_usuario=user)
        reservacion_queryset = Reservacion.objects.filter(id_periodo=vacaciones)
        if reservacion_queryset.exists(): #and reservacion_usuario.exists():
            raise ValidationError("El ususario ya registro su reservacion en este periodo vacacional")
        serializer.save(id_periodo=vacaciones)
        #serializer.save(id_usuario=user)

class ReservacionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReservacionUser]
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer


