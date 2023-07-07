from rest_framework import serializers

from .models import Sale

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def save(self):
        sale = Sale(product=self.validated_data['product'],
                    supplier = self.validated_data['supplier'],
                    imei=self.validated_data['imei'],
                    picked_at_shop=self.validated_data['picked_at_shop'],
                    delivered_to_client_by=self.validated_data['delivered_to_client_by'],
                    client_name = self.validated_data['client_name'],
                    client_phone_number=self.validated_data['client_phone_number'],
                    client_email=self.validated_data['client_email'],
                    client_location=self.validated_data['client_location'],
                    client_pin=self.validated_data['client_pin'],
                    sold_by=self.validated_data['sold_by'],
                    status=self.validated_data['status'],
                    warranty_status=self.validated_data['warranty_status'],
                    cash=self.validated_data['cash'],
                    mpesa=self.validated_data['mpesa'],
                    invoiced_amount=self.validated_data['invoiced_amount'],
                    expense_name=self.validated_data['expense_name'],
                    expense_amount=self.validated_data['expense_amount']
                    )
        sale.save()
        return sale
    
class UpdateSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
    
class GetSaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id','product','supplier','imei','delivered_to_client_by','client_name','status','cash','mpesa','invoiced_amount']

class GetSingleSaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            'product',
            'supplier', 
            'imei',
            'picked_at_shop',
            'delivered_to_client_by', 
            'client_name',
            'client_phone_number',
            'client_email', 
            'client_location',
            'client_pin',
            'sold_by', 
            'status',
            'warranty_status',
            'cash',
            'mpesa',
            'invoiced_amount',
            'expense_name',
            'expense_amount'
        ]