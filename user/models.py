from django.db import models

class userInfoTable(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    refercode=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now=True)
