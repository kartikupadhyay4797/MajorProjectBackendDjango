from .models import dealerInfoTable
from rest_framework import serializers
class dealerInfoSerialiser(serializers.ModelSerializer):
    class Meta:
        model=dealerInfoTable
        fields=['id','name','address','email','imageURL','date_created']