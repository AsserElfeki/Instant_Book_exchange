from django.core.serializers import serialize
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator
from django_countries.serializer_fields import CountryField
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.models import BookReader, ProfileImage
from boookzdata.models import Book
from versatileimagefield.serializers import VersatileImageFieldSerializer

class ProfileImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(sizes='product_headshot')

    class Meta:
        model = ProfileImage
        fields = ['image', 'book_reader']

class BookReaderSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    profile_image = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = BookReader
        fields = ['username', 'country', 'profile_image']

#For some reason I had problems there when using OneToOneField
#Also wtf I did there
    def get_profile_image(self, obj):
        images = ProfileImage.objects.filter(book_reader=obj)
        serializer = ProfileImageSerializer(images, context=self.context, many=True).data
        image =next(iter(serializer or []), None) 
        image = image if image is None else image['image']['full_size']
        return image

    def get_username(self, obj):
        return obj.user.username

class ListBookReaderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=serializers.CurrentUserDefault()
    )
    books = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BookReader
        fields = ('user', 'books')

    def get_books(self, instance):
        books = Book.objects.all().filter(book_owner=instance)
        return serialize('json', books)


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()
        return instance


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):

        data = super().validate(attrs)
        book_reader = BookReader.objects.get(user=self.user)
        if not book_reader.is_verified or book_reader.is_banned:
            error_message = "This profile wasn't activated"
            error_name = "inactive_profile"
            raise AuthenticationFailed(error_message, error_name)
        return data

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name' )
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
