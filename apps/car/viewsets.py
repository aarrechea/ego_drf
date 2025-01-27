""" Imports """
from django.db import transaction
from django.db.models import Q
from requests.exceptions import HTTPError
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.abstract.viewsets import AbstractViewSet
from apps.auth.permissions import UserPermission
from apps.car.filters import CarFilter
from apps.car.models import Car, CarFeature
from apps.car.serializers import CarSerializer
from apps.features.models import Feature
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view



""" Car viewset """
class CarViewSet(AbstractViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']
    permission_classes = (AllowAny, )
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
    #http://127.0.0.1:8000/api/car/?type__in=1,2
    """ filterset_fields = {
        'type': ["in"]
    } """
    filterset_class = CarFilter
    
    
    # Get queryset decorated with drf-spectacular
    @extend_schema(
    parameters=[
        OpenApiParameter(
            name="data",
            description=(
                "Type of car:\n"
                "   - zero to list all cars.\n"
                "   - one to list only autos.\n"
                "   - two to list Pickup and Comerciales.\n"
                "   - three to list Suvs and Crossovers. "
            ),
            type=int,
        )
    ])
    def get_queryset(self):
        return super().get_queryset()
    
    
        
    # List            
    """     queryset = Car.objects.all()                
        param = int(self.request.query_params.get('data'))
                
        if self.request.query_params.get('data'):
            param = int(self.request.query_params.get('data'))
            
            if param > 0 and param < 4:
                if param == 1:
                    queryset = queryset.filter(type=param)
                else:
                    if param == 2:
                        type_one = 2
                        type_two = 3
                        
                    elif param == 3:
                        type_one = 4
                        type_two = 5
                    
                    queryset = queryset.filter(Q(type=type_one) | Q(type=type_two))
            
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data) """
    

    
    # Get object
    def get_object(self):
        obj = Car.objects.get_object_by_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    # Create
    def create(self, request, *args, **kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def destroy(self, request, *args, **kwargs):
        self.media_file.delete()                
        return super().destroy(request, *args, **kwargs)
    