from rest_framework import serializers
from .models import Product

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name','buying_price','selling_price','date_purchased','paid_for','good_condition','shop')


