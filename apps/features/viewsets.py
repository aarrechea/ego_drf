""" Imports """
from requests.exceptions import HTTPError
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.abstract.viewsets import AbstractViewSet
from apps.auth.permissions import UserPermission
from apps.features.models import Feature
from apps.features.serializers import FeatureSerializer



""" Feature viewset """
class FeatureViewSet(AbstractViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (UserPermission, )
    serializer_class = FeatureSerializer
    
    
    def get_queryset(self):
        queryset = Feature.objects.all()
        return queryset
    
    
    def get_object(self):
        obj = Feature.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    def create(self, request, *args, **kwargs):                                
        serializer = self.get_serializer(data=request.data)                        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        