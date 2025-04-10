from djoser.serializers import UserCreateSerializer as \
                              BaseUserCreateSerializer \
                            , UserSerializer as \
                            BaseUserSerializer

from .models import User
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    """Custom user creation serializer."""
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(BaseUserSerializer):
    """Custom user serializer."""
    class Meta(BaseUserSerializer.Meta):
        fields = ('id', 'email', 'role', 'first_name', 'last_name')
    
    def validate_role(self, value):
        # Ensure the role is either Vendor or Customer
        if value not in [User.VENDOR, User.CUSTOMER]:
            raise serializers.ValidationError("Role must be either Vendor or Customer.")
        return value

    
