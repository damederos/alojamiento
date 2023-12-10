from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        staff_permission = bool(request.user and (request.user.is_staff or request.user.is_superuser))
        return staff_permission

class ReservacionUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #valida si es staff o admin
        admin_permission = bool(request.user.is_staff or request.user.is_superuser)
        usuario = obj.id_usuario == request.user
        permitido = bool(admin_permission or usuario)
        return permitido