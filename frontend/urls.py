from django.urls import path
from .views import HomeView, SignInView, RegisterView

urlpatterns = [
    path('', HomeView),
    path('signin/', SignInView),
    path('register/', RegisterView),
]
