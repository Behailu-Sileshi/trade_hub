from djoser.serializers import UserCreateSerializer as \
                              BaseUserCreateSerializer \
                            , UserSerializer as \
                            BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    """Custom user creation serializer."""
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

class UserSerializer(BaseUserSerializer):
    """Custom user serializer."""
    class Meta(BaseUserSerializer.Meta):
        fields = ('id', 'username', 'email', 'password', 'role')
        read_only_fields = ('id',)