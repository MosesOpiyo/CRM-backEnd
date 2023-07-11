from rest_framework import serializers
from .models import Service_Center,Device,Comment

from Stock.models import Stock
from Stock.serializers import StockSerializers

class ServiceCenterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service_Center
        fields = ['service_center_name']

    def save(self):
        service_center = Service_Center(
            service_center_name=self.validated_data['service_center_name'],
            )
        service_center.save()
        return service_center

class CommentSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

    def save(self):
        comment = Comment(
            comment=self.validated_data['comment'],
            )
        comment.save()
        return comment
class DeviceSerializers(serializers.ModelSerializer):
    device = StockSerializers(read_only=True)
    comment = CommentSeriailizer(many=True)
    class Meta:
        model = Device
        fields = ['device','user_damage','user_damage_comment','amount','taken_by','taken_date','comment','issue','service_center_feedback','status']

    def save(self,imei):
        device = Stock.objects.select_related('service_center_feedback').get(imei=imei)
        stock = Device(
            device = device,
            user_damage=self.validated_data['user_damage'],
            user_damage_comment=self.validated_data['user_damage_comment'],
            amount=self.validated_data['amount'],
            taken_by=self.validated_data['taken_by'],
            taken_date=self.validated_data['taken_date'],
            comment=self.validated_data['comment'],
            issue=self.validated_data['issue'],
            status=self.validated_data['status']
            )
        stock.save()
        return stock
    
class UpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['user_damage','user_damage_comment','amount','taken_by','taken_date','issue','service_center_feedback','status']
    
class GetDeviceSerializers(serializers.ModelSerializer):
    device = StockSerializers(read_only=True)
    comment = CommentSeriailizer(many=True)
    class Meta:
        model = Device
        fields = '__all__'

class GetServiceCenterSerializers(serializers.ModelSerializer):
    devices =  GetDeviceSerializers(many=True)
    class Meta:
        model = Service_Center
        fields = '__all__'