from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user_model 
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import *
from .serializer import *

class MerchantList(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    def get(self, request, format=None):
        all_users =  get_user_model().objects.all()
        serializers = MerchantSerializer(all_users, many=True)
        return Response(serializers.data)
from rest_framework.response import Response
    def post(self, request, format=None):
        serializers = MerchantSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagerList(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    def get(self, request, format=None):
        all_users =  get_user_model().objects.all()
        serializers = ManagerSerializer(all_users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ManagerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ClerkList(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    def get(self, request, format=None):
        all_users =  get_user_model().objects.all()
        serializers = ClerkSerializer(all_users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ClerkSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SoloMerchant(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    def get_Merch(self, pk):
        try:
            return get_user_model().objects.get(pk=pk)
        except get_user_model().DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        Merch = self.get_Merch(pk)
        serializers = MerchantSerializer(Merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        Merch = self.get_Merch(pk)
        serializers = MerchantSerializer(Merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Merch = self.get_Merch(pk)
        Merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SoloManager(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    def get_Manager(self, pk):
        try:
            return get_user_model().objects.get(pk=pk)
        except get_user_model().DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        Manager = self.get_Manager(pk)
        serializers = ManagerSerializer(Manager)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        Manager = self.get_Manager(pk)
        serializers = ManagerSerializer(Manager, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Manager = self.get_Manager(pk)
        Manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SoloClerk(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    def get_Clerk(self, pk):
        try:
            return get_user_model().objects.get(pk=pk)
        except get_user_model().DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        Clerk = self.get_Clerk(pk)
        serializers = ManagerSerializer(Clerk)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        Clerk = self.get_Clerk(pk)
        serializers = ClerkSerializer(Clerk, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Clerk = self.get_Clerk(pk)
        Clerk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductBatchList(APIView):

    serializer_class = ProductBatchSerializer

    def get(self, request, format=None):
        snippets = ProductBatch.objects.all()
        serializer = ProductBatchSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_batch_data = request.data

        new_product_batch = ProductBatch.objects.create(
            item=Item.objects.get(id=product_batch_data["item"]), 
            buying_price=product_batch_data["buying_price"], 
            # date_received=product_batch_data["date_received"], 
            damaged_items=product_batch_data["damaged_items"], 
            supplier=Supplier.objects.get(id=product_batch_data["supplier"]),
            clerk=Clerk.objects.get(id=product_batch_data["clerk"]),
            payment_status=product_batch_data["payment_status"]
            )

        new_product_batch.save()

        serializer = ProductBatchSerializer(new_product_batch)

        return Response(serializer.data)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT) 

