from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PetViewset,PetTypeViewset,AdoptionViewset,PetList,PetDetails,AdoptPetAPIView


router = DefaultRouter()
router.register('list',PetViewset)
router.register('types',PetTypeViewset)
router.register('adoption',AdoptionViewset)
 
 
urlpatterns = [
    path('', include(router.urls)),
    path('adopt/<int:pet_id>', AdoptPetAPIView.as_view(),name='adopt_pet'),
    path('post/', PetList.as_view(),name='post_pet'),
    path('post/<int:pk>/', PetDetails.as_view(),name='details_pet'),
]
  