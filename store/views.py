from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *

class ProductBunchList(APIView):
    def get(self, request, format=None):
        all_product = Product_Bunch.objects.all()
        serializers = ProductBunchSerializer(all_product, many=True)
        return Response(serializers.data)

