from rest_framework import serializers
from django.contrib.auth.models import User
from user_app.models import Persona

class RegistrationsSerrializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Persona
        fields = ['usuario', 'correo', 'password', 'password2', 'nombre_completo', 'ci', 'telefono']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error': 'Las contraseñas no coinciden'})
        if Persona.objects.filter(correo=self.validated_data['correo']).exists():
            raise serializers.ValidationError({'error': 'El correo ya existe'})
        account = Persona.objects.create_user(
            nombre_completo=self.validated_data['nombre_completo'],
            usuario=self.validated_data['usuario'],
            password=self.validated_data['password'],
            ci=self.validated_data['ci'],
            correo=self.validated_data['correo']
        )
        account.set_password=self.validated_data['password']
        account.telefono = self.validated_data['telefono']
        account.save()
        return account
