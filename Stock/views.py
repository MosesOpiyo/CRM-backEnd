from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Stock
from .serializers import *

class stockClass:
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def postStock(request):
        serializer = StockSerializers(data=request.data)
        data = {}
        
        if serializer.is_valid():
            serializer.save()
            data = "Stock Successfully added"
            return Response(data,status=status.HTTP_201_CREATED)
        
    @api_view(["PUT"])
    @permission_classes([IsAuthenticated])
    def editStock(request,id):
        sale = get_object_or_404(Stock, pk=id)
        serializer = StockSerializers(data=request.data)
        data = {}

        if serializer.is_valid(): 
            data = {
            "product":serializer.validated_data['product'],
            "supplier":serializer.validated_data['supplier'],
            "imei":serializer.validated_data['imei'],
            "checked_in_person_name":serializer.validated_data['checked_in_person_name'],
            "warranty_duration":serializer.validated_data['warranty_duration'],
            "amount":serializer.validated_data['amount'] 
            }
            serializer.update(instance=sale,validated_data=data)
            
            
            return Response(data,status=status.HTTP_202_ACCEPTED)
        else:
            data = serializer.errors
            print(serializer.errors)
            return Response(data,status=status.HTTP_400_BAD_REQUEST)

    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def allStocks(request):
        data = {}
        
        stocks = Stock.objects.all()
        data = GetStockSerializer(stocks,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def singleStock(request,id):
        data = {}
        
        stock = Stock.objects.get(id=id)
        data = GetStockSerializer(stock).data
        return Response(data,status=status.HTTP_200_OK)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def allStockValue(request):
        data = {}
        
        stock = Stock.objects.all()
        data = GetStockSerializer(stock,many=True).data
        return Response(data,status=status.HTTP_200_OK)
