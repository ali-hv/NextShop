from django.contrib import admin
from django.urls import path

from .views import ListProduct, DetailProduct

app_name = 'products'

urlpatterns = [
    path("<int:pk>/", DetailProduct.as_view(), name="product_detail"),
    path("", ListProduct.as_view(), name="products_list"),
]