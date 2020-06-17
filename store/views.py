from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *

class ProductList(APIView):
    def get(self, request, format=None):
        all_product = Product.objects.all()
        serializers = Productserializer(all_product, many=True)
        return Response(serializers.data)

