from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import regitration


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', regitration, name='register')
]