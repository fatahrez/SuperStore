from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

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
