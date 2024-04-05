from django.contrib import admin
from django.urls import path

from .views import ListProduct

app_name = 'products'

urlpatterns = [
    path("", ListProduct.as_view(), name="products_list")
]