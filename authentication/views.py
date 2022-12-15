import jwt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import BookReader
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, ListBookReaderSerializer, \
    ProfileInfoSerializer
from rest_framework import generics, status
from django.contrib.auth.models import User

from .utils import Util


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

    def post(self, request, *args, **kwargs):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data["email"])
        data = self.get_verification_email_data(request, user)
        Util.send_email(data=data)
        return Response({"response": f"{data}"},status=status.HTTP_200_OK)

    @staticmethod
    def get_verification_email_data(request, user):
        token = RefreshToken.for_user(user)
        relative_link = reverse('email-verify')
        current_site = get_current_site(request)
        abs_url = f'http://{current_site}{relative_link}?token={str(token)}'
        email_body = f'Hi {user.username} Use link below to verify your email\n{abs_url}'
        data = {"to_email": (user.email,),"email_body": email_body, "email_subject": "Verify your email"}
        return data


class EmailVerify(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            book_reader = BookReader.objects.get(user=user)
            if not book_reader.is_verified:
                book_reader.is_verified = True
                book_reader.save()
            return Response({"response": "Successfully activated"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as ex:
            return Response({"response": "Activation expired"}, status=status.HTTP_400_BAD_REQUEST)
        # except jwt.DecodeError as ex:
        #     return Response({"response": f"Invalid token{token}"}, status=status.HTTP_400_BAD_REQUEST)




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
