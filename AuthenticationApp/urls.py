from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from .views import LoginViewSet


ROUTER = DefaultRouter()


ROUTER.register(
    r'login',
    LoginViewSet,
    basename='login'
)

urlpatterns = [
    path('', include(ROUTER.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
