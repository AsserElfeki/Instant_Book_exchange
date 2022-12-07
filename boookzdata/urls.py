from django.urls import path, include

from .views import BookViewSet, ImageViewSet, BookUploadView, BooksFromChosenBookshelfView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book', BookViewSet, basename='Book')
router.register('image', ImageViewSet, basename='Image')
# router.register(r'shelf/giveaway', BooksFromGiveawayBookshelfView, basename='GiveawayBookshelf')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/<str:bookshelf>', BookUploadView.as_view(), name='upload'),
    path('shelf/<str:bookshelf>', BooksFromChosenBookshelfView.as_view(), name='GiveawayBookshelf')
]
