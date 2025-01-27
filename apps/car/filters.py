# Imports
import django_filters
from apps.car.models import Car
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view



# Filterset
class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            'type': ["in"]
        }
        