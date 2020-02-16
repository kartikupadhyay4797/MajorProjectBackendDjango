from .models import OrderInfoTable
from rest_framework import serializers
class OrderInfoSerialiser(serializers.ModelSerializer):
    class Meta:
        model=OrderInfoTable
        fields=['id','orderCreatedDate','orderItems','orderItemsQuantity','orderItemsPrice','orderItemsTotalPrice','orderTotalPrice','orderStatus','orderByUser','orderToDealer','orderReviewText','orderReviewStarRating','orderWithPromocode','orderPaymentMethod','orderPaymentStatus']