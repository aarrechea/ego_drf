# Imports
from rest_framework import serializers
from apps.abstract.serializers import AbstractSerializer
from apps.user.models import User



# User serializer
class UserSerializer(AbstractSerializer):    
    class Meta:
        model = User
        fields = [
            'id',
            'created',
            'updated',
            'email',
            'first_name',
            'last_name',
            'photo',                        
            'user_type',
            'is_staff',
            'is_superuser',
            'is_active'
        ]
        
        
        



