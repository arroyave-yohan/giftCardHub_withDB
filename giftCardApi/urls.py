from django.urls import path, include
from .views import (
    giftCardListApiView,
    GiftCardDetailApiView,
)

urlpatterns = [
    path('api', giftCardListApiView.as_view()),
    path('api/<int:giftCard_id>/', GiftCardDetailApiView.as_view()),
]