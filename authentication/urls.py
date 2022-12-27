from django.urls import path, include

from authentication.views import ProfileInfoView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, \
    LogoutAllView, ListBookReaderBooks, EmailVerify, LoginView
from rest_framework_simplejwt.views import TokenRefreshView 

from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        ]

router = CustomReadOnlyRouter()
router.register('profile', ProfileInfoView)
urlpatterns = router.urls

urlpatterns = [
    path('list/', ListBookReaderBooks.as_view({'get':'list'}), name='list_book_reader'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('email-verify/', EmailVerify.as_view(), name='email-verify'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_passowrd'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('', include(router.urls)),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]
