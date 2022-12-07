from django.core.serializers import serialize
from rest_flex_fields import FlexFieldsModelSerializer

from authentication.models import BookReader
from authentication.serializers import BookReaderSerializer
from .models import Book, Category, Author, BookCondition, BookSite, User, Comment, Image, GiveawayBookshelf, BookShelf, WantedBookshelf
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework import serializers


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']


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


class WantedBookShelfSerializer(FlexFieldsModelSerializer):
    shelf_owner = BookReaderSerializer(read_only=True)

    class Meta:
        model = WantedBookshelf
        fields = '__all__'


class GiveawayBookshelfSerializer(FlexFieldsModelSerializer):
    shelf_owner = BookReaderSerializer(read_only=True)

    class Meta:
        model = GiveawayBookshelf
        fields = '__all__'


class BookUploadSerializer(FlexFieldsModelSerializer):
    name = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    # TODO: image
    # TODO: category
    book_shelf = BookShelfSerializer(required=False)

    class Meta:
        model = Book
        fields = ['pk', 'name', 'content', 'created', 'updated', 'book_shelf']
        expandable_fields = {
            'category': ('boookzdata.CategorySerializer', {'many': True}),
            'sites': ('boookzdata.BookSiteSerializer', {'many': True}),
            'comments': ('boookzdata.CommentSerializer', {'many': True}),
            'image': ('boookzdata.ImageSerializer', {'many': True}),
        }


class BookSerializer(FlexFieldsModelSerializer):
    name = serializers.CharField(required=False)
    content = serializers.CharField(required=False)

    class Meta:
        model = Book
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('boookzdata.CategorySerializer', {'many': True}),
            'sites': ('boookzdata.BookSiteSerializer', {'many': True}),
            'comments': ('boookzdata.CommentSerializer', {'many': True}),
            'image': ('boookzdata.ImageSerializer', {'many': True}),
        }


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
