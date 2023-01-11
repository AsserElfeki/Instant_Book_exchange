from django_countries.serializer_fields import CountryField
from itertools import chain
from django_countries.serializers import CountryFieldMixin
from rest_flex_fields import FlexFieldsModelSerializer

from authentication.models import BookReader, ProfileImage, Notification
from authentication.serializers import BookReaderSerializer, ProfileImageSerializer
from transactions.serializers import TransactionRatingSerializerView
from .models import Book, Category, Author, BookCondition, User, Comment, Image, BookShelf, ReportRecord
from transactions.models import Transaction, TransactionStatus, TransactionRating
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
    book_shelf = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'language', 'description', 'category', 'condition', 'images', 'book_owner',
                  'created', 'book_shelf',]

    def get_book_shelf(self, obj):
        serializer = BookShelfSerializer(obj.book_shelf)
        return serializer.data['shelf_name']

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
    class Meta:
        model = BookShelf
        fields = ['shelf_name', ]


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


# Not the bast code but had to be done so frontend is happy. Maybe there is other way
class TransactionStatusSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = ['name', ]


class TransactionForProfileSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=False, max_length=64)
    book_reader_initiator = serializers.SerializerMethodField()
    book_reader_receiver = serializers.SerializerMethodField()
    initiator_book = serializers.SerializerMethodField()
    receiver_book = serializers.SerializerMethodField()
    transaction_status = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = (
            'token', 'book_reader_initiator', 'book_reader_receiver', 'initiator_book', 'receiver_book',
            'transaction_status', 'created', 'modified')

    def get_transaction_status(self, obj):
        name = TransactionStatusSerializer(obj.transaction_status, read_only=True, context=self.context).data['name']
        return name
    
    def get_book_reader_initiator(self, obj):
        init_reader = BookReaderSerializer(obj.book_reader_initiator, context=self.context).data
        return init_reader['username'] if init_reader is not None else init_reader 

    def get_book_reader_receiver(self, obj):
        receive_reader = BookReaderSerializer(obj.book_reader_receiver, context=self.context).data
        return receive_reader['username'] if receive_reader is not None else receive_reader 

    def get_initiator_book(self, obj):
        init_book = BookSerializer(obj.initiator_book, context=self.context).data
        return init_book['title'] if init_book is not None else init_book 

    def get_receiver_book(self, obj):
        receive_book = BookSerializer(obj.receiver_book, context=self.context).data
        return receive_book['title'] if receive_book is not None else receive_book 

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['pk', 'content', 'origin', 'book_reader', 'modified']


class ReportRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportRecord
        fields = ['message', 'book_reader', 'created', ]


class ProfileInfoSerializer(CountryFieldMixin, FlexFieldsModelSerializer):
    profile_image = serializers.SerializerMethodField()
    wanted_books = serializers.SerializerMethodField()
    giveaway_books = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    transactions = serializers.SerializerMethodField()
    notifications = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = BookReader
        fields = ['country', 'profile_image', 'languages', 'wanted_books', 'giveaway_books', 'transactions', 'ratings',
                  'notifications', ]

    def getKey(self, e):
        return e['modified']

    def get_ratings(self, obj):
        book_reader = BookReader.objects.get(user=obj.user)
        book_reader_transaction_rating = TransactionRating.objects.filter(book_reader=book_reader)
        serialized = TransactionRatingSerializerView(book_reader_transaction_rating, context=self.context, many=True).data

        ser_list = list(chain(serialized))
        ser_list.sort(reverse=True, key=self.getKey)
        return ser_list

    def get_notifications(self, obj):
        book_reader = BookReader.objects.get(user=obj.user)
        book_reader_notifications = Notification.objects.filter(book_reader=book_reader)
        serialized = NotificationSerializer(book_reader_notifications, context=self.context, many=True).data

        ser_list = list(chain(serialized))
        ser_list.sort(reverse=True, key=self.getKey)
        return ser_list

    def get_transactions(self, obj):
        book_reader = BookReader.objects.get(user=obj.user)
        user_transactions_as_initiator = Transaction.objects.filter(book_reader_initiator=book_reader)
        serializer = TransactionForProfileSerializer(user_transactions_as_initiator, context=self.context,
                                                     many=True).data
        user_transactions_as_receiver = Transaction.objects.filter(book_reader_receiver=book_reader)
        serializer2 = TransactionForProfileSerializer(user_transactions_as_receiver, context=self.context,
                                                      many=True).data
        transactions = list(chain(serializer, serializer2))
        
        transactions.sort(reverse=True, key=self.getKey)

        return transactions

    def get_profile_image(self, obj):
        images = ProfileImage.objects.filter(book_reader=obj)
        serializer = ProfileImageSerializer(images, context=self.context, many=True).data
        image = next(iter(serializer or []), None)
        image = image if image is None else image['image']['full_size']
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
