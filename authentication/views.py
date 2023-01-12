import jwt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import BookReader, Notification, ProfileImage
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, ListBookReaderSerializer, LoginSerializer, ProfileImageSerializer
from boookzdata.serializers import UserSerializer
from rest_framework import generics, status
from django.contrib.auth.models import User

from .utils import Util


# Create your views here.

class ProfilePictureUpload(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileImageSerializer

    def post(self, request, *args, **kwarg):
        if request.data.get('image') is None:
            return Response({"error": "image cannot be empty"})
        image_data = {"image": request.data.get('image')}
        book_reader = BookReader.objects.get(user=request.user).pk
        reader = {"book_reader": book_reader}

        prev_images = ProfileImage.objects.filter(book_reader=book_reader)
        prev_images.delete()

        data = {**image_data, **reader}
        image = self.serializer_class(data=data)
        if image.is_valid(raise_exception=True):
            image.save()
            return Response({"success": "image uploaded"})
        
        return Response({"error": "failed to upload an image"})


class ProfileInfoView(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def retrive(self, request):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, id=self.request.user.id)
        serializer_class = UserSerializer(user, context=self.get_serializer_context()) 
        return Response(serializer_class.data)

class AnyProfileInfoView(ReadOnlyModelViewSet):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def retrive(self, request, username=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, username=username)
        serializer_class = UserSerializer(user, context=self.get_serializer_context()) 
        return Response(serializer_class.data)

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

class DeleteAllNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        book_reader = BookReader.objects.get(user=user)
        notifications = Notification.objects.filter(book_reader=book_reader)
        notifications.delete()

        return Response({"result": "notifications deleted"})


class DeleteNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        book_reader = BookReader.objects.get(user=user)
        notifications = Notification.objects.filter(book_reader=book_reader)
        notification_to_delete = notifications.get(id=self.kwargs['pk'])
        notification_to_delete.delete()

        return Response({"result": "notification deleted"})

class DeleteAccount(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()

        return Response({"result": "user deleted"})

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        user = request.data
        country = request.data.get("country")
        if country is None or len(country) > 2:
            return Response({"error": "country field"})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data["email"])
        book_reader = BookReader.objects.get(user=user)
        country = request.data.get("country")
        if country is None or len(country) > 2:
            return Response({"error": "country field"})
        book_reader.country = country 
        book_reader.save()
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
        frontend_ip = f"http://{request.get_host()}:3000/profileactivated"
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            book_reader = BookReader.objects.get(user=user)
            if not book_reader.is_verified:
                book_reader.is_verified = True
                book_reader.save()
            return redirect(frontend_ip)
        except jwt.ExpiredSignatureError as ex:
            return redirect(reverse(frontend_ip))
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
