from django.urls import path, include

from .views import BookViewSet, ImageViewSet, BookUploadView, SearchGiveAwayBooksView, AllWantedView, AllGiveawayView, \
    WantedInSameCountryView, GiveawayInSameCountryView, DeleteBookView, ReportRecordView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book', BookViewSet, basename='Book')
router.register('image', ImageViewSet, basename='Image')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/<str:bookshelf_param>', BookUploadView.as_view(), name='upload'),
    path('wanted/', AllWantedView.as_view(), name='WantedBooks'),
    path('giveaway/', AllGiveawayView.as_view(), name='GiveawayBooks'),
    path('wanted/country/', WantedInSameCountryView.as_view(), name='WantedBooksInSameCountry'),
    path('giveaway/country/', GiveawayInSameCountryView.as_view(), name='GiveawayBooksInSameCountry'),
    path('search', SearchGiveAwayBooksView.as_view(), name=' SearchGiveAwayBooks'),
    path('delete/<int:pk>', DeleteBookView.as_view(), name='DeleteBook'),
    path('report/', ReportRecordView.as_view(), name='ReportRecord'),
]
