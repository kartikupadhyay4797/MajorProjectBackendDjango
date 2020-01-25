from rest_framework import viewsets
from .serializers import dealerInfoSerialiser
from .models import dealerInfoTable

class DealerViewSet(viewsets.ModelViewSet):
    queryset = dealerInfoTable.objects.all().order_by('-date_created')
    serializer_class = dealerInfoSerialiser