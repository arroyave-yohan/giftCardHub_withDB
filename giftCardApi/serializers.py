from rest_framework import serializers
from .models import giftCard
class giftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = giftCard
        fields = ["id", "client", "provider", "balance", "redemptionToken", "redemptionToken", "emissionDate", "expiringDate"]