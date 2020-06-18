from rest_framework import serializers
from .models import *

class ProductBatchSerializer(serializers.ModelSerializer):
    # item1 = serializers.CharField(source='item.item_name', read_only=True)
    # supplier1 = serializers.CharField(source='supplier.supplier_name', read_only=True)
    # clerk1 = serializers.CharField(source='clerk.first_name', read_only=True)

    class Meta:
        model = ProductBatch
        fields = (
            'id',
            'item',
            'buying_price',
            'date_received',
            'damaged_items',
            'supplier',
            'clerk',
            'payment_status'
            )
        depth = 3
        