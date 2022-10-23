from django.db import models
from django.contrib.auth.models import User

class giftCard(models.Model):
    client = models.EmailField(max_length = 64, blank = False, null = False)
    balance = models.IntegerField(blank = False, null = False)
    
    def __str__(self):
        return self.task