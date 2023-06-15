from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import viewsets
from app.models import *
from app.serializers import *

@permission_classes([IsAuthenticated])
class ProductCrudMVS(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer