from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework import generics, status, filters
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from authentication.models import BookReader
from .serializers import BookSerializer, BookUploadSerializer, GiveawayBookshelfSerializer, ImageSerializer
from .models import Book, Image, GiveawayBookshelf, WantedBookshelf
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class NotCorrectUrlProvided(APIException):
    status_code = 503
    default_detail = 'Not correct url is provided, expected data/upload/wanted or data/upload/giveaway'
    default_code = 'service_unavailable'


class SearchGiveAwayBooksView(ListAPIView):
    serializer_class = BookSerializer
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
    filter_backends = [filters.SearchFilter]
    search_fields = ("^name",) #TODO search by author, category, etc

    def get_queryset(self):
        giveaway_shelves = GiveawayBookshelf.objects.all()
        queryset = Book.objects.all().filter(book_shelf__in=giveaway_shelves)
        return queryset


class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class BookViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permit_list_expands = ['category', 'condition',]
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Book.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'condition'):
            queryset = queryset.prefetch_related('condition')

        return queryset

#TODO(drago): 2 views for all wanted and all giveaway
class AllGiveawayView(FlexFieldsModelViewSet):
    serializer_class = BookSerializer
    queryset = GiveawayBookshelf

class BooksFromChosenBookshelfView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Book.objects.all()
        if queryset:
            book_reader = BookReader.objects.get(user=self.request.user)
            if self.kwargs['bookshelf'] == "giveaway":
                giveaway_bookshelves = GiveawayBookshelf.objects.all()
                users_bookshelf = giveaway_bookshelves.filter(book_reader=book_reader)
                users_books = queryset.filter(book_shelf_id__in=users_bookshelf)
                return users_books
            elif self.kwargs['bookshelf'] == "wanted":
                wanted_bookshelves = WantedBookshelf.objects.all()
                users_bookshelf = wanted_bookshelves.filter(book_reader=book_reader)
                users_books = queryset.filter(book_shelf_id__in=users_bookshelf)
                return users_books
            else:
                raise NotCorrectUrlProvided()
        return queryset


class BookUploadView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookUploadSerializer

    def perform_create(self, serializer):
        book_reader = BookReader.objects.get(user=self.request.user)
        if self.kwargs['bookshelf'] == "giveaway":
            giveaway_bookshelf = GiveawayBookshelf.objects.get(book_reader=book_reader)
            serializer.save(book_shelf=giveaway_bookshelf)
        elif self.kwargs['bookshelf'] == "wanted":
            wanted_bookshelf = WantedBookshelf.objects.get(book_reader=book_reader)
            serializer.save(book_shelf=wanted_bookshelf)
        else:
            raise NotCorrectUrlProvided()

    def get_queryset(self):
        return super().get_queryset().filter(
            bookshelf=self.kwargs['bookshelf']
        )
