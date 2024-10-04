from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewset,ReviewViewSet,UserRegistrationApiView,UserLoginApiView,UserLogoutApiView,activate,PasswordChangeView,ReviewCreateView


router = DefaultRouter()
router.register('list',CustomerViewset)
router.register('review',ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(),name='register'),
    path('login/', UserLoginApiView.as_view(),name='login'),
    path('logout/', UserLogoutApiView.as_view(),name='logout'),
    path('pass_change/', PasswordChangeView.as_view(),name='pass_change'),
    path('create_review/', ReviewCreateView.as_view(),name='create_review'),
    path('active/<uid64>/<token>/', activate, name = 'activate'),
]