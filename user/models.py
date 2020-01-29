from django.db import models
import string
import random
import uuid

class userInfoTable(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=5,default=str(''.join(random.choices(string.ascii_uppercase +string.digits, k = 5))))
#uuid.uuid4().hex[:6].upper())


    refercode=models.CharField(max_length=100,blank=True)
    date_created=models.DateTimeField(auto_now=True)
