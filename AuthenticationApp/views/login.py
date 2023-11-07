from rest_framework import viewsets

from AuthenticationApp.models import Login
from AuthenticationApp.serializers import LoginSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
