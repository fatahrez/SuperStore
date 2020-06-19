from rest_framework import serializers
from rest_framework.serializers import *
from django.contrib.auth import get_user_model
from .models import *
from django.db.models import Q

UserModel = get_user_model()

class MerchantSerializer(serializers.ModelSerializer):
      
    def create(self, validated_data):   
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']     
        )
        user.set_password(validated_data['password'])
        user.save()
        Merchant.objects.create(profile=user)
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password","email","first_name","last_name"  )
        write_only_fields = ('password',)
        read_only_fields = ('id',)


class ManagerSerializer(serializers.ModelSerializer):
  
    def create(self, validated_data):   
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']     
        )
        user.set_password(validated_data['password'])
        user.save()
        Manager.objects.create(profile=user)
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password","email","first_name","last_name"  )
        write_only_fields = ('password',)
        read_only_fields = ('id',) 

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'id',
            'shop_name',
            'manager',
            )
        depth = 3

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