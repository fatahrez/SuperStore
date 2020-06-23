from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.serializers import *
from django.contrib.auth import get_user_model
from .models import *
from django.db.models import Q


UserModel  = get_user_model

class MerchantSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
        )
    
    class Meta:
        model = Merchant
        fields = [
            "id",
            "username", 
            "password", 
            "is_superuser", 
            "is_staff", 
            "email", 
            "first_name", 
            "last_name",
            "token"
            ]
        read_only_fields = (
            'id',
            'is_superuser',
            'is_staff',
            )


    def create(self, validated_data):
        return Merchant.objects.create_merchant(**validated_data)



class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'id',
            'shop_name',
            'manager',
            )
        depth = 3

class ManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
        )
    
    class Meta:
        model = Manager
        fields = [
            "id",
            "username", 
            "password",
            "email",
            "first_name", 
            "is_superuser", 
            "is_staff", 
            "last_name",
            "shop",
            "token"
            ]
        read_only_fields = (
            'id', 
            'is_superuser',
            'is_staff',
            )


    def create(self, validated_data):
        return Manager.objects.create_manager(**validated_data)

class ClerkSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
    max_length=128,
    min_length=8,
    write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = Clerk
        fields = [
            "id",
            "username", 
            "is_superuser", 
            "is_staff", 
            "password",
            "email",
            "first_name",
            "last_name",
            "shop",
            "token"
            ]
        read_only_fields = (
            'id',
            'is_superuser',
            'is_staff',
            )


    def create(self, validated_data):
        return Clerk.objects.create_clerk(**validated_data)

class UserLoginSearilizer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'password is required to login'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with email and password is required to login'
            )

    
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
  

class ProductBatchSerializer(serializers.ModelSerializer):
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
            'payment_status',
            )
        depth = 3
        
class MerchantActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['is_active',]

class ManagerActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['is_active',]

class ClerkActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerk
        fields = ['is_active',]