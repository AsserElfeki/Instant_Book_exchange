from django.urls import path, include

from .views import BookViewSet, ImageViewSet, BookUploadView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='Book')
router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/<str:bookshelf>', BookUploadView.as_view(), name='upload'),
]
