from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from authentication.models import BookReader
from .serializers import BookSerializer, ImageSerializer, BookUploadSerializer, GiveawayBookshelfSerializer
from .models import Book, Image, GiveawayBookshelf, WantedBookshelf
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class NotCorrectUrlProvided(APIException):
    status_code = 503
    default_detail = 'Not correct url is provided, expected data/upload/wanted or data/upload/giveaway'
    default_code = 'service_unavailable'


class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]


class BookViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Book.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        if is_expanded(self.request, 'sites'):
            queryset = queryset.prefetch_related('sites')

        if is_expanded(self.request, 'author'):
            queryset = queryset.prefetch_related('sites__author')

        if is_expanded(self.request, 'bookcondition'):
            queryset = queryset.prefetch_related('sites__bookcondition')

        return queryset


class BooksFromGiveawayBookshelfViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Book.objects.all()
        if queryset:
            giveaway_bookshelves = GiveawayBookshelf.objects.all()
            book_reader = BookReader.objects.get(user=self.request.user)
            users_bookshelf = giveaway_bookshelves.filter(book_reader=book_reader)
            users_books = queryset.filter(book_shelf_id__in=users_bookshelf)
            return users_books
        return queryset


class BookUploadView(generics.CreateAPIView):
    queryset = Book.objects.all()
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
