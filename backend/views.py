from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializer import UserSerializer


class ImageCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

