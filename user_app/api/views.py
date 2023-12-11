from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationsSerrializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth

@api_view(['POST'])
def regitration(request):
    if request.method == 'POST':
        serializer = RegistrationsSerrializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'El registro ha sido exitoso'
            data['username'] = account.username
            data['email'] = account.email
            data['nombre_completo']= account.nombre_completo
            #me devuelve un token en base64
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    data = {}
    if request.method=='POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
    persona = auth.authenticate(usuario=usuario, password=password)
    if persona is not None:
        data['response'] = 'Se ha logeado'
        data['usuario'] = persona.usuario
        data['nombre_completo'] = persona.nombre_completo
        data['correo'] = persona.correo
        data['ci'] = persona.ci
        refresh = RefreshToken.for_user(persona)
        data['token'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(data)
    else:
        data['error'] = "Credenciales incorrectas"
        return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)