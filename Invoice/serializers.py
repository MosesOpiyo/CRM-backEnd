from rest_framework import serializers
from .models import *
from Stock.serializers import GetStockSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['supplier_name','amount','PO_number','due_date','balance','pay_this_money_from','payment_method','cheque_no_or_ref','invoice_date','invoice_number','amount_paid']

    def save(self):
        invoice = Invoice(
            supplier_name=self.validated_data['supplier_name'],
            amount=self.validated_data['amount'],
            PO_number = self.validated_data['PO_number'],
            due_date = self.validated_data['due_date'],
            balance = self.validated_data['balance'],
            pay_this_money_from = self.validated_data['pay_this_money_from'],
            payment_method = self.validated_data['payment_method'],
            cheque_no_or_ref = self.validated_data['cheque_no_or_ref'],
            invoice_date = self.validated_data['invoice_date'],
            invoice_number = self.validated_data['invoice_number'],
            amount_paid = self.validated_data['amount_paid']
        )
        invoice.save()
        return invoice
    
class GetInvoiceSerializer(serializers.ModelSerializer):
    items = GetStockSerializer(many=True)
    class Meta:
        model = Invoice
        fields = '__all__'