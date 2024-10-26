from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PetViewset,PetTypeViewset,AdoptionViewset,PetList,PetDetails,InitiatPaymentAPIView,PaymentSuccessAPIView,PaymentFailAPIView,PaymentCancelAPIView


router = DefaultRouter()
router.register('list',PetViewset)
router.register('types',PetTypeViewset)
router.register('adoption',AdoptionViewset)
 
 
urlpatterns = [
    path('', include(router.urls)),
    # path('adopt/<int:pet_id>', AdoptPetAPIView.as_view(),name='adopt_pet'),
    path('payment/initiat/<int:pet_id>/', InitiatPaymentAPIView.as_view(),name='initiat_payment'),
    path('payment/success/<int:pet_id>/', PaymentSuccessAPIView.as_view(),name='payment_success'),
    path('payment/failed/', PaymentFailAPIView.as_view(),name='payment_failed'),
    path('payment/cancel/', PaymentCancelAPIView.as_view(),name='payment_cancel'),
    path('post/', PetList.as_view(),name='post_pet'),
    path('post/<int:pk>/', PetDetails.as_view(),name='details_pet'),
]
  