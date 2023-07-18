from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Sale
from .serializers import SalesSerializers,GetSaleSerializers,GetSingleSaleSerializers,UpdateSaleSerializer

class SaleClass:
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def newSale(request):
        serializer = SalesSerializers(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data = "New Sale Added"
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            print(serializer.errors)
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        
    @api_view(["PUT"])
    @permission_classes([IsAuthenticated])
    def editSale(request,id):
        sale = get_object_or_404(Sale, pk=id)
        serializer = SalesSerializers(data=request.data)
        data = {}

        if serializer.is_valid(): 
            data = {
            'product':serializer.validated_data['product'],
            'supplier':serializer.validated_data['supplier'],
            'imei':serializer.validated_data['imei'],
            'picked_at_shop':serializer.validated_data['picked_at_shop'],
            'delivered_to_client_by':serializer.validated_data['delivered_to_client_by'],
            'client_name':serializer.validated_data['client_name'],
            'client_phone_number':serializer.validated_data['client_phone_number'],
            'client_email':serializer.validated_data['client_email'],
            'client_location':serializer.validated_data['client_location'],
            'client_pin':serializer.validated_data['client_pin'],
            'sold_by':serializer.validated_data['sold_by'], 
            'status':serializer.validated_data['status'],
            'warranty_status':serializer.validated_data['warranty_status'],
            'cash':serializer.validated_data['cash'],
            'mpesa':serializer.validated_data['mpesa'],
            'invoiced_amount':serializer.validated_data['invoiced_amount'],
            'expense_name':serializer.validated_data['expense_name'],
            'expense_amount':serializer.validated_data['expense_amount'],
            }
            serializer.update(instance=sale,validated_data=data)
            
            
            return Response(data,status=status.HTTP_202_ACCEPTED)
        else:
            data = serializer.errors
            print(serializer.errors)
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def allSales(request):
        data = {}
        sales = Sale.objects.all()
        data = GetSaleSerializers(sales,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def allSalesAtShop(request):
        data = {}
        sales = Sale.objects.filter(status='At The Shop')
        data = GetSaleSerializers(sales,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def allSalesClients(request):
        data = {}
        clients = []
        sales = Sale.objects.all()
        for sale in sales:
            if sale.client_name not in clients:
                clients.append(sale.client_name)
        data = clients
        print(clients)
        return Response(data,status=status.HTTP_200_OK)
    
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def singleSales(request,id):
        data = {}
        sales = Sale.objects.get(id=id)
        data = GetSingleSaleSerializers(sales).data
        return Response(data,status=status.HTTP_200_OK)
    
