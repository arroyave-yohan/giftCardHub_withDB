from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class giftCard(models.Model):
    client = models.EmailField(max_length = 64, blank = False, null = False)
    #provider = models.CharField(max_length = 64, blank = False, null = False)
    balance = models.IntegerField(blank = False, null = False)
    #redemptionToken = models.CharField(max_length = 64, blank = False)
    #redemptionCode = models.CharField(max_length = 64, blank = False)
    #emissionDate = models.CharField(max_length = 64, blank = False)
    #expiringDate = models.CharField(max_length = 64, blank = False)
    
    def __str__(self):
        return self.task