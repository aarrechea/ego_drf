# Imports
from rest_framework import viewsets, filters



# Abstract viewset
class AbstractViewSet(viewsets.ModelViewSet):
    #filter_backends = ['filters.OrderingFilter']
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']