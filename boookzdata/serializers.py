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
        fields = ['name', ]


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        expandable_fields = {
            'products': ('boookzdata.BookSerializer', {'many': True})
        }

class BookConditionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = BookCondition
        fields = ['name']

class BookShelfSerializer(FlexFieldsModelSerializer):
    book_reader = BookReaderSerializer()

    class Meta:
        model = GiveawayBookshelf
        fields = ['book_reader', ]

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
        sizes=[
            ('full_size', 'url'),
            ]
    )

    class Meta:
        model = Image
        fields = ['image',]

class BookSerializer(FlexFieldsModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    condition = BookConditionSerializer(required=False)
    images = ImageSerializer(many=True)
    # author = AuthorSerializer(many=True) 
    category = CategorySerializer(many=True)
    book_owner = serializers.SerializerMethodField() 
#TODO(Victor/drago): Give me book_owner of this book
    class Meta:
        model = Book
        fields = ['pk', 'title', 'description', 'category', 'created', 'updated', 'condition', 'images', 'book_owner',]

    def get_book_owner(self, obj):
        return obj.get_book_reader().user.username


        # expandable_fields = {
            # 'category': ('boookzdata.CategorySerializer', {'many': True}),
        # }
    # def get_images(self, obj):
        # images = Image.objects.all().filter(book=obj)
        # serializer = ImageSerializer(images, context = self.context)
        # return serializer.data 

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
    wanted_shelf = serializers.SerializerMethodField()
    giveaway_shelf = serializers.SerializerMethodField()

    class Meta:
        model = BookReader
        fields = ['user', 'country', 'profile_image', 'wanted_shelf', 'giveaway_shelf']

    def get_wanted_shelf(self, obj):
        book_shelves = WantedBookshelf.objects.get(book_reader=obj)
        serializer = WantedBookShelfSerializer(book_shelves, context = self.context)
        return serializer.data 

    def get_giveaway_shelf(self, obj):
        book_shelves = GiveawayBookshelf.objects.get(book_reader=obj)
        serializer = GiveawayBookshelfSerializer(book_shelves, context = self.context)
        return serializer.data 
