from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, nombre_completo, ci, usuario, correo, password=None):
        if not nombre_completo:
            raise ValueError('El usuario debe tener nombre')
        if not ci:
            raise ValueError('El usuario debe tener carnet de indentidad')
        if not usuario:
            raise ValueError('El usuario debe tener nombre de usuario')
        if not correo:
            raise ValueError('El usuario debe tener correo')
        user = self.model(
            correo= self.normalize_email(correo),
            usuario=usuario,
            nombre_completo=nombre_completo,
            ci=ci,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_completo, ci, usuario, correo, password=None):
        user = self.create_user(
            correo=self.normalize_email(correo),
            usuario=usuario,
            nombre_completo=nombre_completo,
            ci=ci,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superadmin=True
        user.is_active=True
        user.save(using=self._db)
        return user

class Persona(AbstractBaseUser):
    id_persona = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_completo = models.CharField(max_length=150, null=False, blank=False)
    ci = models.CharField(max_length=32, null=False, blank=False, unique=True)
    usuario = models.CharField(max_length=50, unique=True, null=False, blank=False)
    correo = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    telefono = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nombre_completo', 'ci', 'correo']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.nombre_completo}'

    def __str__(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

