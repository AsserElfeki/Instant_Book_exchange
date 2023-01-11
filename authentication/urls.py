from django.urls import path

from authentication.views import ProfileInfoView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, \
    LogoutAllView, ListBookReaderBooks, EmailVerify, LoginView, DeleteAccount, AnyProfileInfoView, DeleteNotification, DeleteAllNotification, ProfilePictureUpload
from rest_framework_simplejwt.views import TokenRefreshView 

urlpatterns = [
    path('list/', ListBookReaderBooks.as_view({'get':'list'}), name='list_book_reader'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('email-verify/', EmailVerify.as_view(), name='email-verify'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_passowrd'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('delete/', DeleteAccount.as_view(), name="profile_delete"),
    path('notification_delete/<int:pk>', DeleteNotification.as_view(), name="notification_delete"),
    path('notification_delete_all/', DeleteAllNotification.as_view(), name="notification_delete_all"),
    path('profile/', ProfileInfoView.as_view({'get': 'retrive'}), name="profile_info"),
    path('profile/<str:username>', AnyProfileInfoView.as_view({'get': 'retrive'}), name="any_profile_info"),
    path('upload_profile_image/', ProfilePictureUpload.as_view(), name="profile_picture_upload"),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]
