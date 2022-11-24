from rest_flex_fields import FlexFieldsModelSerializer
from .models import Book, Category, Author, BookCondition, BookSite, User, Comment, Image
from versatileimagefield.serializers import VersatileImageFieldSerializer

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


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'boookzdata.CategorySerializer',
            'user': 'boookzdata.UserSerializer'
        }
