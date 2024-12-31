# Imports
from rest_framework import routers
from apps.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from apps.car.viewsets import CarViewSet
from apps.user.viewsets import UserViewSet




# Router declaration
router = routers.SimpleRouter()



# Auth
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')



# Car
router.register(r'car', CarViewSet, basename='car')



# User
router.register(r'user', UserViewSet, basename='user')



# Patterns
urlpatterns = [
    *router.urls
]