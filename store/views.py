from django.shortcuts import render,redirect
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user_model 
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .serializer import *
from .renderers import UserJSONRenderer
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from .models import *


class MerchantRegistration(APIView):
    permission_classes =  [ permissions.AllowAny ]
    renderer_classes = (UserJSONRenderer,)
    serializer_class = MerchantSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ManagerRegistration(APIView):
    permission_classes =  [ permissions.AllowAny ]
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ManagerSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        current_site=get_current_site(request)
        new_mail = user['email']
        new_user = User.objects.get(email=new_mail)
        print(new_user.pk)
        user=new_user
        message = render_to_string('auth/activate.html',
        {
        'user':user,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
        'token':generate_token.make_token(user)
        }
        )
        email_message = EmailMessage(
        'Superstore registration confirmation' ,   
        message,
        settings.EMAIL_HOST_USER,
        [new_mail],
        )
        email_message.send() 
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ActivateAccountView(View):
    def get (self,request,uidb64,token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('login')


         
       

class ClerkRegistration(APIView):
    permission_classes =  [ permissions.AllowAny]
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ClerkSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLogin(APIView):
    permission_classes = [ permissions.AllowAny]
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserLoginSearilizer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
    def get_Clerk(self, pk):
        try:
            return get_user_model().objects.get(pk=pk)
        except get_user_model().DoesNotExist:
            return Http404
           
    def get(self, request, pk, format=None):
        Clerk = self.get_Clerk(pk)
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



class ItemList(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = ItemSerializer
    def get(self, request, format=None):
        all_items =  Item.objects.all()
        serializers = ItemSerializer(all_items, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ItemSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseList(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = ProductBatchSerializer
    def get(self, request, format=None):
        all_items =  ProductBatch.objects.all()
        serializers = ProductBatchSerializer(all_items, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProductBatchSerializer(data=request.data)
        order = request.data
        item = Item.objects.get(shop=order["shop"],item_name=order["item"])
        item.quantity = item.quantity+order["quantity_bought"]
        item.save()
        print(item.quantity)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SalesList(APIView):
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = ProductSalesSerializer
    def get(self, request, format=None):
        all_items =  ProductSales.objects.all()
        serializers = ProductSalesSerializer(all_items, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProductSalesSerializer(data=request.data)
        sale = request.data
        item = Item.objects.get(shop=sale["shop"],item_name=sale["item"])
        item.quantity = item.quantity-sale["quantity"]
        item.save()
        print(item.quantity)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)





