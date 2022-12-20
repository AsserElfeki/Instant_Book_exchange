from django.core.serializers import serialize
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework_simplejwt.authentication import authentication

from authentication.models import BookReader
from authentication.serializers import BookReaderSerializer, UserSerializer
from .models import Book, Category, Author, BookCondition, BookSite, User, Comment, Image, GiveawayBookshelf, BookShelf, WantedBookshelf
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework import serializers


class AuthorSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Author
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
            'products': ('boookzdata.BookSerializer', {'many': True})
        }

class BookConditionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = BookCondition
        fields = ['pk', 'name']

class BookShelfSerializer(FlexFieldsModelSerializer):
    shelf_owner = BookReaderSerializer(read_only=True)

    class Meta:
        model = GiveawayBookshelf
        fields = '__all__'

class BookUploadSerializer(FlexFieldsModelSerializer):
    name = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    book_shelf = BookShelfSerializer(required=False)

    class Meta:
        model = Book
        fields = ['pk', 'name', 'content', 'created', 'updated', 'book_shelf']
        expandable_fields = {
            'category': ('boookzdata.CategorySerializer', {'many': True}),
            'comments': ('boookzdata.CommentSerializer', {'many': True}),
        }

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['name', 'image',]


class BookSerializer(FlexFieldsModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    condition = BookConditionSerializer(required=False)
    images = ImageSerializer(many=True)

    class Meta:
        model = Book
        fields = ['pk', 'title', 'description', 'created', 'updated', 'condition', 'images']
        expandable_fields = {
            'category': ('boookzdata.CategorySerializer', {'many': True}),
        }

class GiveawayBookshelfSerializer(FlexFieldsModelSerializer):
    shelf_owner = BookReaderSerializer(read_only=True)
    books = BookSerializer(many=True)

    class Meta:
        model = GiveawayBookshelf
        fields = ['shelf_owner', 'books']

class WantedBookShelfSerializer(FlexFieldsModelSerializer):
    shelf_owner = BookReaderSerializer(read_only=True)
    books = BookSerializer(many=True)

    class Meta:
        model = WantedBookshelf
        fields = ['shelf_owner', 'books']

class BookSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = BookSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'book': 'boookzdata.CategorySerializer',
            'bookcondition': 'boookzdata.BookConditionSerializer',
            'author': 'boookzdata.AuthorSerializer',
        }


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'boookzdata.CategorySerializer',
            'user': 'boookzdata.UserSerializer'
        }

class ProfileInfoSerializer(FlexFieldsModelSerializer):
    user = UserSerializer(read_only=True)
    profile_image = ImageSerializer(read_only=True)

    class Meta:
        model = BookReader
        fields = ['user', 'profile_image',]

