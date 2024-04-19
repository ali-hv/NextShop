from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem


class CartDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        # Get the cart for the current user
        return self.queryset.get(user=self.request.user)


class CartItemList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        # Get the cart items list for the current user
        return self.queryset.filter(cart__user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(cart=request.user.cart)  # Assign the cart to the current user's cart
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_object(self):
        # Raise 404 error if the CartItem object doesn't belong to the user
        obj = super().get_object()
        if obj.cart.user != self.request.user:
            raise Http404({"detail": "No CartItem matches the given query."})
        return obj
