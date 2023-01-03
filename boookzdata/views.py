from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework import generics, status, filters
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import APIView, action

from authentication.models import BookReader
from .serializers import BookSerializer, BookUploadSerializer, GiveawayBookshelfSerializer, ImageSerializer, \
    WantedBookShelfSerializer
from .models import Book, Image, GiveawayBookshelf, WantedBookshelf, BookCondition, Category, Author
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


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
        giveaway_shelves = GiveawayBookshelf.objects.all()
        queryset = Book.objects.all().filter(book_shelf__in=giveaway_shelves)
        return queryset


class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    # permission_classes = (IsAuthenticated,)
    queryset = Image.objects.all()

    @action(detail=False, methods=['post'])
    def upload(request):
        try:
            file=request.data['image']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        product=Image.objects.create(image=file)


class BookViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permit_list_expands = ['category', 'condition', ]
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Book.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'condition'):
            queryset = queryset.prefetch_related('condition')

        if is_expanded(self.request, 'author'):
            queryset = queryset.prefetch_related('author')

        return queryset


class AllGiveawayView(ListAPIView):
    serializer_class = BookSerializer
    

    def get_queryset(self):
        giveaway_shelves = GiveawayBookshelf.objects.all()
        giveaway_books = Book.objects.filter(book_shelf_id__in=giveaway_shelves)
        return giveaway_books


class AllWantedView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        wanted_shelves = WantedBookshelf.objects.all()
        wanted_books = Book.objects.filter(book_shelf_id__in=wanted_shelves)
        return wanted_books


# TODO(Victor): Think about code below xD
class BooksFromChosenBookshelfView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Book.objects.all()
        if queryset:
            book_reader = queryset.get(user=self.request.user)
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


class GiveawayBookUploadView(APIView):
    def post(self, request):
        title = {"title": request.data.get('title')}
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
        bookshelf = {"book_shelf": GiveawayBookshelf.objects.get(book_reader=book_reader["book_reader"]).pk}
        data= {**title, **description, **authorsList, **categoriesList, **book_reader, **bookshelf, **condition}

        serializer = BookUploadSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()

        image_data = {"image": request.data.get("image"), "book": book_saved.pk}
        image_serializer = ImageSerializer(data=image_data)
        if image_serializer.is_valid(raise_exception=True):
            image_saved = image_serializer.save()
        return Response({"success": "Book '{}' created successfully with image '{}'".format(book_saved, image_saved)})


class WantedBookUploadView(APIView):
    pass

# class BookUploadView(generics.CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    # serializer_class = BookUploadSerializer

    # def perform_create(self, serializer):
        # book_condition = BookCondition.objects.get(name=self.request.data.get("condition"))
        # author, created = Author.objects.get_or_create(name__in=self.request.data.getlist("author"))
        # book_reader = BookReader.objects.get(user=self.request.user)
        # book_categories = Category.objects.filter(name__in=self.request.data.getlist("category"))
        # # for category in book_categories:
            # # cat, created = Category.objects.get_or_create(name=category)
        # if self.kwargs['bookshelf'] == "giveaway":
            # giveaway_bookshelf = GiveawayBookshelf.objects.get(book_reader=book_reader)
            # serializer.save(category=book_categories.pk, condition=book_condition.pk, book_shelf=giveaway_bookshelf)
        # elif self.kwargs['bookshelf'] == "wanted":
            # wanted_bookshelf = WantedBookshelf.objects.get(book_reader=book_reader)
            # serializer.save(category=book_categories.pk, condition=book_condition.pk, book_shelf=wanted_bookshelf)
        # else:
            # raise NotCorrectUrlProvided()

    # def get_queryset(self):
        # return super().get_queryset().filter(
            # bookshelf=self.kwargs['bookshelf']
        # )
