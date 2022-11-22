from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import UserCreateSerializer, UserSerializer, LoginSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        return qs


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['status'] == 200:
            user = serializer.validated_data['user']
            return Response(status.HTTP_200_OK)
        elif serializer.validated_data['status'] == 404:
            return Response(status.HTTP_400_BAD_REQUEST)