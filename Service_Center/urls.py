from django.urls import path
import Service_Center.views as service

urlpatterns = [
    path("newCenter",service.service.newCenter,name="newCenter"),
    path("newDevice/<int:imei>",service.service.newDevice,name="new"),
    path("editSale/<int:id>",service.service.editDevice,name="update"),
    path("allCenters",service.service.allCenters,name="all"),
    path("addDevice/<int:serviceId>/<int:imei>",service.service.addDevice,name="add"),
    path("singleCenter/<int:id>",service.service.singleCenter,name="single"),
    path("singleDevice/<int:id>",service.service.singleDevice,name="single_device")

]