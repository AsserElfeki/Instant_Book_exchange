from django.urls import path, include

from .views import AllGiveawayView, BookViewSet, ImageViewSet, GiveawayBookUploadView, WantedBookUploadView, BooksFromChosenBookshelfView, SearchGiveAwayBooksView, AllWantedView, AllGiveawayView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book', BookViewSet, basename='Book')
router.register('image', ImageViewSet, basename='Image')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/giveaway', GiveawayBookUploadView.as_view(), name='uploadGiveaway'),
    path('upload/wanted', WantedBookUploadView.as_view(), name='uploadWanted'),
    path('shelf/<str:bookshelf>', BooksFromChosenBookshelfView.as_view(), name='GiveawayBookshelf'),
    path('wanted/', AllWantedView.as_view(), name='WantedBooks'),
    path('giveaway/', AllGiveawayView.as_view(), name='GiveawayBooks'),
    path('search', SearchGiveAwayBooksView.as_view(), name=' SearchGiveAwayBooks')
]
