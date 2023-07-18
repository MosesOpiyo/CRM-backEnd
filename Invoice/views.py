from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice 
from .serializers import *

class Invoices:
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def newInvoice(request):
        serializer = InvoiceSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data = "Invoice added."
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            data = serializer.error_messages
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def getInvoices(request):
        data = {}

        invoices = Invoice.objects.all()
        data = GetInvoiceSerializer(invoices,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def singleInvoice(request,id):
        data = {}
        invoice = Invoice.objects.get(id=id)
        data = GetInvoiceSerializer(invoice).data
        return Response(data,status=status.HTTP_200_OK)