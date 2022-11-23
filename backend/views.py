import re

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView

from .models import User
from .serializer import UserCreateSerializer, UserSerializer, UsernameSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        return qs


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        serializer = UsernameSerializer(data=self.request.data,
                                        context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['status'] == 200:
            user = serializer.validated_data['user']
            return HttpResponse(f"You are welcome {user.username}")
        elif serializer.validated_data['status'] == 404:
            return HttpResponse("You are not welcome")
