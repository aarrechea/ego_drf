""" Imports """
from django.db.models import Q
from requests.exceptions import HTTPError
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.abstract.viewsets import AbstractViewSet
from apps.auth.permissions import UserPermission
from apps.car.models import Car
from apps.car.serializers import CarSerializer
from drf_spectacular.utils import OpenApiParameter, extend_schema



""" Car viewset """
class CarViewSet(AbstractViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (AllowAny, )
    serializer_class = CarSerializer
    
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="data",
                description=(
                    "Type of car, zero to three"
                ),
                type=int,
            )
        ]
    )
    def get_queryset(self):                        
        queryset = Car.objects.all()
        
        try:
            param = int(self.request.query_params.get('data'))
            
            if param is not None:
                if param == 0:
                    return queryset
                
                if param == 1:                
                    queryset = queryset.filter(type=param)
                    return queryset
                    
                elif param == 2:
                    type_one = 2
                    type_two = 3                                
                    
                else:
                    type_one = 4
                    type_two = 5
                            
                queryset = queryset.filter(Q(type=type_one) | Q(type=type_two))
                return queryset
        except:                            
            return queryset
        
    
    def get_object(self):
        obj = Car.objects.get_object_by_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    def create(self, request, *args, **kwargs):                                        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        