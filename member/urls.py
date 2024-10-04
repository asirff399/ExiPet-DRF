from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MemberViewset

router = DefaultRouter()
router.register('',MemberViewset)

urlpatterns = [
    path('',include(router.urls)),
] 