from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DealerStockInfoSerialiser
from .models import DealerStockInfoTable

class DealerStockViewSet(viewsets.ModelViewSet):
    queryset = DealerStockInfoTable.objects.all().order_by('dealer_id')
    serializer_class = DealerStockInfoSerialiser