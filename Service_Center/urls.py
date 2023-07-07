from django.urls import path
import Service_Center.views as service

urlpatterns = [
    path("newDevice/<int:imei>",service.service.newDevice,name="new"),
    path("allCenters",service.service.allCenters,name="all"),
    path("singleCenter/<int:id>",service.service.singleCenter,name="single"),
    path("singleDevice/<int:id>",service.service.singleDevice,name="single_device")
]