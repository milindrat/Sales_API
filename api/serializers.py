from rest_framework import serializers
from .models import *

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['internalId', 'documentNumber', 'date']  
