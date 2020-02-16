from django.db import models
from user.models import userInfoTable
from dealer.models import dealerInfoTable

# Create your models here.
class OrderInfoTable(models.Model):
    orderCreatedDate=models.DateTimeField(auto_now=True)
    orderItems=models.CharField(max_length=200)
    orderItemsQuantity=models.CharField(max_length=50)
    orderItemsPrice=models.CharField(max_length=200)
    orderItemsTotalPrice=models.CharField(max_length=200)
    orderTotalPrice=models.CharField(max_length=10)
    orderStatus=models.CharField(max_length=50,default="Not Confirmed By Dealer")
    orderByUser=models.ForeignKey(userInfoTable,on_delete=models.CASCADE,null=False)
    orderToDealer=models.ForeignKey(dealerInfoTable,on_delete=models.CASCADE,null=False)
    orderReviewText=models.CharField(max_length=200,blank=True)
    orderReviewStarRating=models.CharField(max_length=1,blank=True)
    orderWithPromocode=models.CharField(max_length=100,blank=True)
    orderPaymentMethod=models.CharField(max_length=100)
    orderPaymentStatus=models.CharField(max_length=100)
    #dealer_id=models.ForeignKey(dealerInfoTable,on_delete=models.CASCADE,null=False)

