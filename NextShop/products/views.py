from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
