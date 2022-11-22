from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import serializers, status

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'login',
            'password',
        ]


class UserSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            existing_user = User.objects.all().filter(login=username, password=password)
            if existing_user:
                attrs['user'] = existing_user
                attrs['status'] = 200

                return attrs
            else:
                attrs['status'] = 404
                return attrs
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')


