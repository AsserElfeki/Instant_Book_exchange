from django.core.serializers import serialize
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework_simplejwt.authentication import authentication

from authentication.models import BookReader
from authentication.serializers import BookReaderSerializer
from .models import Book, Category, Author, BookCondition, BookSite, User, Comment, Image, GiveawayBookshelf, WantedBookshelf
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
    condition = serializers.SerializerMethodField()
    # images = ImageSerializer(many=True)
    images = serializers.SerializerMethodField()
    # author = AuthorSerializer(many=True) 
    category = serializers.SerializerMethodField()
    book_owner = serializers.SerializerMethodField() 

    class Meta:
        model = Book
        fields = ['pk', 'title', 'description', 'category', 'created', 'updated', 'condition', 'images', 'book_owner',]

    def get_images(self, obj):
        images = Image.objects.filter(book=obj)
        serializer = ImageSerializer(images, many=True).data
        return [item['image']['full_size'] for item in serializer]

    def get_condition(self, obj):
        serializer = BookConditionSerializer(obj.condition)
        return serializer.data['name']

    def get_category(self, obj):
        category = Category.objects.filter(books=obj)
        serializer = CategorySerializer(category, many=True).data
        return [item['name'] for item in serializer]

    def get_book_owner(self, obj):
        profile_image = ImageSerializer(obj.get_book_reader().profile_image, read_only=True).data
        return [obj.get_book_reader().user.username, profile_image['image']['full_size']]

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

class UserSerializer(serializers.ModelSerializer):
    book_reader = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'email', 'book_reader']

    def get_book_reader(self, obj):
        book_reader = BookReader.objects.get(user=obj)
        serializer = ProfileInfoSerializer(book_reader, context= self.context)
        return serializer.data

class ProfileInfoSerializer(FlexFieldsModelSerializer):
    profile_image = serializers.SerializerMethodField()
    wanted_shelf = serializers.SerializerMethodField()
    giveaway_shelf = serializers.SerializerMethodField()

    class Meta:
        model = BookReader
        fields = ['country', 'profile_image', 'wanted_shelf', 'giveaway_shelf']
    
    def get_profile_image(self, obj):
        image = ImageSerializer(obj.profile_image, read_only=True).data
        return image['image']['full_size']

    def get_wanted_shelf(self, obj):
        book_shelves = WantedBookshelf.objects.get(book_reader=obj)
        serializer = WantedBookShelfSerializer(book_shelves)
        return serializer.data

    def get_giveaway_shelf(self, obj):
        book_shelves = GiveawayBookshelf.objects.get(book_reader=obj)
        serializer = GiveawayBookshelfSerializer(book_shelves)
        return serializer.data
