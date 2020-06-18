from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Merchant, Manager, Clerk

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


# class ClerkSerializer(serializers.ModelSerializer):
  
#     def create(self, validated_data):   
#         user = UserModel.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']     
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         Clerk.objects.create(profile=user)
#         return user

#     class Meta:
#         model = UserModel
#         fields = ( "id", "username", "password","email","first_name","last_name"  )
#         write_only_fields = ('password',)
#         read_only_fields = ('id',)       


