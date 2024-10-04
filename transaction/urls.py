from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DeposiMoneyAPIView,WithdrawMoneyAPIView

router = DefaultRouter()


urlpatterns = [
    path('',include(router.urls)),
    path('deposit/',DeposiMoneyAPIView.as_view(),name='deposit'),
    path('withdraw/',WithdrawMoneyAPIView.as_view(),name='withdraw'),
] 