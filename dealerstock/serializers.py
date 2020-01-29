from .models import DealerStockInfoTable
from rest_framework import serializers
class DealerStockInfoSerialiser(serializers.ModelSerializer):
    class Meta:
        model=DealerStockInfoTable
        fields=['id','item_name','item_capacity','item_rate','item_type','item_quality','dealer_id','date_created']