from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

from .views import LoginViewSet


ROUTER = DefaultRouter()


ROUTER.register(
    r'login',
    LoginViewSet,
    basename='login'
)


urlpatterns = [
    path('', include(ROUTER.urls))
]
