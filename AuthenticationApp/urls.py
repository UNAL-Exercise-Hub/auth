from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter
from .views.token import login
from .views.token import whoAmI

from .views.login import LoginViewSet


ROUTER = DefaultRouter()


ROUTER.register(
    r'login',
    LoginViewSet,
    basename='login'
)

urlpatterns = [
    path('', include(ROUTER.urls)),
    path('token', login),
    path('verifytoken', whoAmI)
]
