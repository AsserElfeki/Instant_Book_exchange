from rest_flex_fields import FlexFieldsModelSerializer
from .models import Book, Category, Author, BookCondition, BookSite, User, Comment, Image
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


class BookSerializer(FlexFieldsModelSerializer):
    book_owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = ['pk', 'name', 'content', 'created', 'updated', 'book_owner']
        expandable_fields = {
            'category': ('boookzdata.CategorySerializer', {'many': True}),
            'sites': ('boookzdata.BookSiteSerializer', {'many': True}),
            'comments': ('boookzdata.CommentSerializer', {'many': True}),
            'image': ('boookzdata.ImageSerializer', {'many': True}),
        }

    def get_book_owner(self, instance):
        self.user


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
