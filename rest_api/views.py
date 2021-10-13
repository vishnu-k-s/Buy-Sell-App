

from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .serializers import RegistrationSerializer
from .serializers import *
from buy_sell.models import Product
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, mixins
from rest_framework.response import Response
from buy_sell.models import NewUser
from buy_sell.models import Product
from buy_sell.models import Category

class Registration(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = RegistrationSerializer


class RegisteredUserList(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = RegisteredUserListSerializer
    
    #permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    