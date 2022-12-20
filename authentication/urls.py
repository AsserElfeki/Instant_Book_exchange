from django.urls import path, include

from authentication.views import ProfileInfoView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, \
    LogoutAllView, ListBookReaderBooks, EmailVerify, LoginView
from rest_framework_simplejwt.views import TokenRefreshView 

urlpatterns = [
    path('list/', ListBookReaderBooks.as_view({'get':'list'}), name='list_book_reader'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('email-verify/', EmailVerify.as_view(), name='email-verify'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_passowrd'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('profiles/', ProfileInfoView.as_view(), name='all_profiles'),
    path('profiles/<str:username>', ProfileInfoView.as_view(), name='all_profiles'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]
