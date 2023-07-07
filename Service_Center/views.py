from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Service_Center,Device
from .serializers import ServiceCenterSerializers,DeviceSerializers,GetServiceCenterSerializers,GetDeviceSerializers
from Stock.models import Stock


# Create your views here.
class service:
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def newDevice(request,imei):
        serializer = DeviceSerializers(data=request.data)
        data = {}
        
        if serializer.is_valid():
            serializer.save(imei=imei)
            data = "New device added for repairs"
            return Response(data,status=status.HTTP_200_OK)
        
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def addDevice(request,serviceId,imei):
        data = {}
        
        serviceCenter = Service_Center.objects.prefetch_related('devices').get(id=serviceId)
        device = Stock.objects.select_related('service_center_feedback').get(imei=imei)
        serviceCenter.devices.add(device)
        serviceCenter.save()
        data = f"New Device {device.product} added to {serviceCenter.service_center_name}"
        return Response(data,status=status.HTTP_202_ACCEPTED)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def allCenters(request):
        data = {}
        centers = Service_Center.objects.all()
        data = GetServiceCenterSerializers(centers,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def singleCenter(request,id):
        data = {}
        centers = Service_Center.objects.get(id=id)
        data = GetServiceCenterSerializers(centers).data
        
        return Response(data,status=status.HTTP_200_OK)
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def singleDevice(request,id):
        data = {}
        centers = Device.objects.get(id=id)
        data = GetDeviceSerializers(centers).data
        
        return Response(data,status=status.HTTP_200_OK)

    

    
