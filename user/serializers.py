from .models import userInfoTable
from rest_framework import serializers
class userInfoSerialiser(serializers.ModelSerializer):
    class Meta:
        model=userInfoTable
        fields=['id','name','address','email','refercode','date_created']