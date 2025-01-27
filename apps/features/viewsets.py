""" Imports """
import os
from django.db import transaction
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
    permission_classes = (AllowAny, )
    serializer_class = FeatureSerializer
    
    
    def get_queryset(self):
        queryset = Feature.objects.all()
        return queryset
    
    
    def get_object(self):
        obj = Feature.objects.get_object_by_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    def create(self, request, *args, **kwargs):                                
        serializer = self.get_serializer(data=request.data)                        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def destroy(self, request, *args, **kwargs):                
        image = Feature.objects.get(id=kwargs['pk'])
        
        try:
            with transaction.atomic():
                delete_image(image.photo)                        
                return super().destroy(request, *args, **kwargs)
        except NameError:
            return Response({'Error':NameError})    
        
                
def delete_image(image_folder):
    folder_path = '/home/adrian/Dropbox/ego-drf-react-project/drf_ego/media/features/feature_None'
    filename =  str(image_folder).rsplit('/', 1)[1]
    
    if filename in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, filename))
    
