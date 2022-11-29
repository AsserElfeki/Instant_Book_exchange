from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet

from authentication.models import BookReader
from .serializers import BookSerializer, ImageSerializer, BookUploadSerializer
from .models import Book, Image
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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


class BookUploadView(generics.CreateAPIView):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookUploadSerializer

    def perform_create(self, serializer):
        name = self.request.query_params.get('name')
        content = self.request.query_params.get('content')
        book_reader = BookReader.objects.get(user=self.request.user)
        serializer.save(book_owner=book_reader, name=name, content=content)
