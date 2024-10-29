from django.urls import path,include
from .views import InitiatePaymentView,payment_cancel,payment_fail,payment_success
# from .views import 

urlpatterns = [
    path('payment/initiate/<int:pet_id>', InitiatePaymentView.as_view(), name='initiate_payment'),
    path('payment/success/<int:user_id>/<int:pet_id>/<int:amount>/<tran_id>', payment_success, name='payment_success'),
    path('payment/fail/', payment_fail, name='payment_fail'),
    path('payment/cancel/', payment_cancel, name='payment_cancel'),
] 