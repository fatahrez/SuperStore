from rest_framework import serializers
from .models import *

class ProductBunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Bunch
        fields = ('product_item_name','buying_price','selling_price','date_purchased','paid_for','spoilt_number_products','shop')


