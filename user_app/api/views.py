from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationsSerrializer
from rest_framework.response import Response
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework import status

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
            #me devuelve un token en base64
            toke = Token.objects.get(user=account).key
            data['token'] = toke
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)