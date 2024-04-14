from rest_framework import generics

from .serializers import ProductSerializer
from .permissions import IsStaffOrReadOnly
from .models import Product


class ProductList(generics.ListCreateAPIView):
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
