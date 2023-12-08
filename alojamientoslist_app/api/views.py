
from alojamientoslist_app.api.serializers import PersonaSerializer
from alojamientoslist_app.models import Persona
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view

#crud de Persona
class PersonaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PersonaDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)