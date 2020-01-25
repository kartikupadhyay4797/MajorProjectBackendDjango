from rest_framework import viewsets
from .serializers import userInfoSerialiser
from .models import userInfoTable

class userViewSet(viewsets.ModelViewSet):
    queryset = userInfoTable.objects.all().order_by('-date_created')
    serializer_class = userInfoSerialiser