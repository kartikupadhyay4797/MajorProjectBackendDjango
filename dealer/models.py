from django.db import models

class dealerInfoTable(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    imageURL=models.CharField(max_length=900)
    date_created=models.DateTimeField(auto_now=True)
