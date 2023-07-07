from rest_framework import serializers
from .models import Stock

class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

    def save(self):
        stock = Stock(
            product=self.validated_data['product'],
            supplier=self.validated_data['supplier'],
            imei=self.validated_data['imei'],
            checked_in_person_name=self.validated_data['checked_in_person_name'],
            warranty_duration = self.validated_data['warranty_duration'],
            amount=self.validated_data['amount'] 
            )
        stock.save()
        return stock
    
class GetStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'