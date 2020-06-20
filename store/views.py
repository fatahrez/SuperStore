from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user_model 
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, Http404,HttpResponseRedirect

from .serializer import MerchantSerializer,ManagerSerializer, ClerkSerializer


class MerchantList(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = MerchantSerializer
    def get(self, request, format=None):
        all_users =  get_user_model().objects.all()
        serializers = MerchantSerializer(all_users, many=True)
        return Response(serializers.data)

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
    serializer_class = ManagerSerializer
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
    serializer_class = ClerkSerializer
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
    serializer_class = MerchantSerializer
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
    serializer_class = ManagerSerializer
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
    serializer_class = ClerkSerializer
    def get_Clerk(self, id):
        try:
            return get_user_model().objects.get(id=id)
        except get_user_model().DoesNotExist:
            return Http404
           
    def get(self, request, id, format=None):
        Clerk = self.get_Clerk(id)
        serializers = ClerkSerializer(Clerk)
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




