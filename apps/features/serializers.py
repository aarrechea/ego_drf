# Imports
from apps.abstract.serializers import AbstractSerializer
from apps.features.models import Feature



# Feature serializer
class FeatureSerializer(AbstractSerializer):    
    class Meta:
        model = Feature
        fields = [
            'id',
            'created',
            'updated',            
            'photo',  
            'designation',
            'title',
            'description',          
        ]
        
        