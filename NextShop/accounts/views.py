from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAdminUser
from rest_framework import generics

from .permissions import IsOwnerOrAdmin
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrAdmin,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
