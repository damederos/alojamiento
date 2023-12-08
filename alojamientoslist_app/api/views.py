
from alojamientoslist_app.api.serializers import (PersonaSerializer, CargoSerializer)
from alojamientoslist_app.models import (Persona, Cargo)
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


