from django.shortcuts import render

from rest_framework import viewsets
from .serializers import OrderInfoSerialiser
from .models import OrderInfoTable
# Create your views here.

class OrderInfoViewSet(viewsets.ModelViewSet):
    queryset = OrderInfoTable.objects.all().order_by('-orderCreatedDate')
    serializer_class = OrderInfoSerialiser
