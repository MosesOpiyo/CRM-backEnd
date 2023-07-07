from rest_framework.decorators import api_view,permission_classes
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
