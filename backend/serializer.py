from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True)
    password=serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'login',
            'password',
        ]
