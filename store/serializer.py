from rest_framework import serializers
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

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'id',
            'shop_name',
            'manager',
            )
        depth = 3


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
            'payment_status'
            )
        depth = 3
        

class UserLoginSerializer(ModelSerializer):
    username = CharField()
    email = EmailField(label='Email Address')
    class Meta:
        model = UserModel
        fields = [
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {
            "password":{"write_only": True},
            }
    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login.")

        user = UserModel.objects.filter(
                    Q(email=email) | 
                    Q(username=username)
                ).distinct()
        
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try valid.")
        return data