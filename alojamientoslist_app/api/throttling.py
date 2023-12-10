from rest_framework.throttling import UserRateThrottle

class ReservacionCreateThrottle(UserRateThrottle):
    scope = 'reservacion-create'