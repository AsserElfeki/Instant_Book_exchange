from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework import generics, status, filters
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import APIView, action

from authentication.models import BookReader
from .serializers import BookSerializer, BookUploadSerializer, ImageSerializer
from .models import Book, Image, BookShelf, BookCondition, Category, Author
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated


class NotCorrectUrlProvided(APIException):
    status_code = 503
    default_detail = 'Not correct url is provided, expected data/upload/wanted or data/upload/giveaway'
    default_code = 'service_unavailable'


class SearchGiveAwayBooksView(ListAPIView):
    serializer_class = BookSerializer
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
    filter_backends = [filters.SearchFilter]
    search_fields = ("^name",)  # TODO search by author, category, etc

    def get_queryset(self):
        giveaway_shelves = BookShelf.objects.filter(shelf_name="giveaway")
        queryset = Book.objects.all().filter(book_shelf__in=giveaway_shelves)
        return queryset


class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Image.objects.all()

class BookViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permit_list_expands = ['category', 'condition', ]
    filterset_fields = ('category', 'language')

    def get_queryset(self):
        queryset = Book.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'condition'):
            queryset = queryset.prefetch_related('condition')

        if is_expanded(self.request, 'author'):
            queryset = queryset.prefetch_related('author')

        return queryset

class GiveawayInSameCountryView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('category', 'language')

    def get_queryset(self):
        giveaway_shelves = BookShelf.objects.filter(shelf_name="giveaway")
        book_reader = BookReader.objects.get(user=self.request.user)
        book_readers_in_country = BookReader.objects.filter(country=book_reader.country)
        giveaway_books = Book.objects.filter(book_shelf_id__in=giveaway_shelves, book_reader__in=book_readers_in_country)
        return giveaway_books


class WantedInSameCountryView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('category', 'language')

    def get_queryset(self):
        wanted_shelves = BookShelf.objects.filter(shelf_name="wanted")
        book_reader = BookReader.objects.get(user=self.request.user)
        book_readers_in_country = BookReader.objects.filter(country=book_reader.country)
        wanted_books = Book.objects.filter(book_shelf_id__in=wanted_shelves, book_reader__in=book_readers_in_country)
        return wanted_books

class AllGiveawayView(ListAPIView):
    serializer_class = BookSerializer
    filterset_fields = ('category', 'language')

    def get_queryset(self):
        giveaway_shelves = BookShelf.objects.filter(shelf_name="giveaway")
        giveaway_books = Book.objects.filter(book_shelf_id__in=giveaway_shelves)
        return giveaway_books


class AllWantedView(ListAPIView):
    serializer_class = BookSerializer
    filterset_fields = ('category', 'language')

    def get_queryset(self):
        wanted_shelves = BookShelf.objects.filter(shelf_name="wanted")
        wanted_books = Book.objects.filter(book_shelf_id__in=wanted_shelves)
        return wanted_books

class BookUploadView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, bookshelf_param):
        title = {"title": request.data.get('title')}
        language = {"language": request.data.get('language')}
        description = {"description": request.data.get('description')}
        authors=[]
        for reqAuth in request.data.getlist("author"):
            aut,created = Author.objects.get_or_create(name=reqAuth)
            authors.append(aut.pk)

        categories=[]
        for reqCat in request.data.getlist("category"):
            cat,created = Category.objects.get_or_create(name=reqCat)
            categories.append(cat.pk)

        authorsList = {"author": authors} 
        categoriesList = {"category": categories}
        condition = {"condition": BookCondition.objects.get(name=request.data.get("condition")).pk}
        book_reader = {"book_reader": BookReader.objects.get(user=request.user).pk}
        if bookshelf_param == "wanted" or bookshelf_param == "giveaway":
            bookshelf = {"book_shelf": BookShelf.objects.get(shelf_name=bookshelf_param).pk}
        else:
            raise NotCorrectUrlProvided()

        data= {**title, **description, **authorsList, **language, **categoriesList, **book_reader, **bookshelf, **condition}
        serializer = BookUploadSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()

        for reqImage in request.data.getlist("image"):
            image_data = {"image": reqImage, "book": book_saved.pk}
            image_serializer = ImageSerializer(data=image_data)
            if image_serializer.is_valid(raise_exception=True):
                image_saved = image_serializer.save()

        return Response({"success": "Book '{}' created successfully with image".format(book_saved)})
