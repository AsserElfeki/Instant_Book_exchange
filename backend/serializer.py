from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True)
    password=serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'login',
            'password',
        ]

class UserSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

