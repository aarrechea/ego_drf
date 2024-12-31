# Imports
from rest_framework import serializers
from apps.user.serializers import UserSerializer
from apps.user.models import User



# Register serializer. Is a subclass of Player serializer, so we do not need to rewrite fields again.
class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
    
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'photo',                        
            'password',
            'user_type',
        ]



