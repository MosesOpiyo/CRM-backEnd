from rest_framework import serializers
from .models import *

class InvoicePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoicePayments
        fields = '__all__'

    def save(self):
        invoice_payment = InvoicePayments(
            supplier_name=self.validated_data['supplier_name'],
            payment_date = self.validated_data['payment_date'],
            pay_this_money_from = self.validated_data['pay_this_money_from'],
            payment_method = self.validated_data['payment_method'],
            cheque_no = self.validated_data['cheque_no'],
            invoice_date = self.validated_data['invoice_date'],
            invoice_number = self.validated_data['invoice_number'],
            current_number = self.validated_data['current_number'],
            amount_paid = self.validated_data['amount_paid']
        )
        invoice_payment.save()
        return invoice_payment