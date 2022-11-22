from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('show/', views.UserListAPIView.as_view()),
]
