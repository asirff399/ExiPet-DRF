from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ContactUsViewset

router = DefaultRouter()
router.register('',ContactUsViewset)

urlpatterns = [
    path('',include(router.urls)),
] 