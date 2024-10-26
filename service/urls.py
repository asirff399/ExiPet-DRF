from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewset

router = DefaultRouter()
router.register('',ServiceViewset)

urlpatterns = [
    path('',include(router.urls)),
] 