from django.urls import path

from .views import CartDetail, CartItemList, CartItemDetail

app_name = 'cart'

urlpatterns = [
    path('', CartDetail.as_view(), name='cart-detail'),
    path('items/', CartItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', CartItemDetail.as_view(), name='item-detail'),
]
