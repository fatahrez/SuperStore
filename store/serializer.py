from rest_framework import serializers
from .models import (Merchant, Manager, Clerk)



class MerchantSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
    max_length=128,
    min_length=8,
    write_only=True
    )
    
    class Meta:
        model = Merchant
        fields = ["id","username", "password","email","first_name","last_name"]
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Merchant.objects.create_merchant(**validated_data)


class ManagerSerializer(serializers.ModelSerializer):
  
    password = serializers.CharField(
    max_length=128,
    min_length=8,
    write_only=True
    )
    
    class Meta:
        model = Manager
        fields = ["id","username", "password","email","first_name","last_name","shop" ]
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Manager.objects.create_manager(**validated_data)



class ClerkSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
    max_length=128,
    min_length=8,
    write_only=True
    )
    
    class Meta:
        model = Clerk
        fields = ["id","username", "password","email","first_name","last_name","shop" ]
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Clerk.objects.create_clerk(**validated_data)
  


    


