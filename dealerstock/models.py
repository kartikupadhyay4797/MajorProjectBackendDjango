from django.db import models
from dealer.models import dealerInfoTable

# Create your models here.

class DealerStockInfoTable(models.Model):
    item_name=models.CharField(max_length=100)
    item_capacity=models.CharField(max_length=100)
    item_rate=models.CharField(max_length=100)
    item_type=models.CharField(max_length=100)
    item_quality=models.CharField(max_length=100)
    dealer_id=models.ForeignKey(dealerInfoTable,on_delete=models.CASCADE,null=False)
    date_created=models.DateTimeField(auto_now=True)
    class Meta:
        unique_together=(('item_rate','item_type','item_quality','dealer_id'),)