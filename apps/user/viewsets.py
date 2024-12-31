# Imports
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets, serializers, response, status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from apps.auth.permissions import UserPermission
from apps.user.models import User
from apps.user.serializers import UserSerializer



# User viewset
class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch', 'get', 'post')
    permission_classes = (UserPermission, )
    serializer_class = UserSerializer
    
    
    def get_queryset(self):        
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.exclude(is_superuser=True)
        
        
    def get_object(self):
        obj = User.objects.get(id=self.kwargs['id'])
        self.check_object_permissions(self.request, obj)        
        return obj

