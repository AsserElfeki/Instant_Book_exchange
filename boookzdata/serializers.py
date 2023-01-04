from rest_flex_fields import FlexFieldsModelSerializer

from authentication.models import BookReader
from authentication.serializers import BookReaderSerializer
from .models import Book, Category, Author, BookCondition, User, Comment, Image, BookShelf
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


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(sizes='product_headshot')

    class Meta:
        model = Image
        fields = ['image', 'book']


class BookSerializer(FlexFieldsModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    condition = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    book_owner = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'language', 'description', 'category', 'condition', 'images', 'book_owner', 'created', ]

    def get_images(self, obj):
        images = Image.objects.filter(book=obj)
        serializer = ImageSerializer(images, context=self.context, many=True).data
        return [item['image']['full_size'] for item in serializer]

    def get_condition(self, obj):
        serializer = BookConditionSerializer(obj.condition)
        return serializer.data['name']

    def get_category(self, obj):
        category = Category.objects.filter(books=obj)
        serializer = CategorySerializer(category, many=True).data
        return [item['name'] for item in serializer]

    def get_author(self, obj):
        author = Author.objects.filter(books=obj)
        serializer = AuthorSerializer(author, many=True).data
        return [item['name'] for item in serializer]

    def get_book_owner(self, obj):
        book_owner = obj.get_book_reader()
        book_owner_serialized = BookReaderSerializer(book_owner, context=self.context).data
        return book_owner_serialized


class BookUploadSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    language = serializers.CharField(max_length=255)
    description = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    condition = serializers.PrimaryKeyRelatedField(queryset=BookCondition.objects.all())
    book_reader = serializers.PrimaryKeyRelatedField(queryset=BookReader.objects.all())
    book_shelf = serializers.PrimaryKeyRelatedField(queryset=BookShelf.objects.all())

    def create(self, validated_data):
        book_instance = Book.objects.create(title=validated_data["title"], 
                                            description=validated_data["description"],
                                            condition=validated_data["condition"],
                                            book_shelf=validated_data["book_shelf"],
                                            book_reader=validated_data["book_reader"],
                                            language=validated_data["language"])
        [book_instance.category.add(category) for category in validated_data['category']]
        [book_instance.author.add(author) for author in validated_data['author']]
        return book_instance

class BookShelfSerializer(FlexFieldsModelSerializer):
    book_reader = BookReaderSerializer(read_only=True)
    books = BookSerializer(many=True)

    class Meta:
        model = BookShelf
        fields = ['book_reader', 'books', ]

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
        serializer = ProfileInfoSerializer(book_reader, context=self.context)
        return serializer.data


class ProfileInfoSerializer(FlexFieldsModelSerializer):
    profile_image = serializers.SerializerMethodField()
    wanted_books = serializers.SerializerMethodField()
    giveaway_books = serializers.SerializerMethodField()

    class Meta:
        model = BookReader
        fields = ['country', 'profile_image', 'wanted_books', 'giveaway_books']

    def get_profile_image(self, obj):
        image = ImageSerializer(obj.profile_image, read_only=True, context=self.context).data['image']
        image = image if image is None else image['full_size']
        return image

    def get_wanted_books(self, obj):
        book_shelf = BookShelf.objects.get(shelf_name="wanted")
        books = Book.objects.filter(book_reader=obj, book_shelf=book_shelf)
        serializer = BookSerializer(books, context=self.context, many=True)
        return serializer.data

    def get_giveaway_books(self, obj):
        book_shelf = BookShelf.objects.get(shelf_name="giveaway")
        books = Book.objects.filter(book_reader=obj, book_shelf=book_shelf)
        serializer = BookSerializer(books, context=self.context, many=True)
        return serializer.data
