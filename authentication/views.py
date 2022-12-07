from django.shortcuts import render
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import BookReader
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, ListBookReaderSerializer, ProfileInfoSerializer
from rest_framework import generics, status
from django.contrib.auth.models import User


# Create your views here.

class ProfileInfoView(ReadOnlyModelViewSet):
    serializer_class = ProfileInfoSerializer

    def get_queryset(self):
        queryset = BookReader.objects.all()
        return queryset

class ListBookReaderBooks(FlexFieldsModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ListBookReaderSerializer

    def get_queryset(self):
        book_readers = BookReader.objects.all()
        return book_readers.filter(user=self.request.user)

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
