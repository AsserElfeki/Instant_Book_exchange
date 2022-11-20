from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializer import UserCreateSerializer, UserSerializer


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
