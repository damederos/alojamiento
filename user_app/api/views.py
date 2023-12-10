from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationsSerrializer
from rest_framework.response import Response

@api_view(['POST'])
def regitration(request):
    if request.method == 'POST':
        serializer = RegistrationsSerrializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)