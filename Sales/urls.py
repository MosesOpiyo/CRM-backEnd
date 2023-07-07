from django.urls import path
import Sales.views as sales

urlpatterns = [
    path("AllSales",sales.SaleClass.allSales,name="all"),
    path("SingleSale/<int:id>",sales.SaleClass.singleSales,name="sale"),
    path("newSale",sales.SaleClass.newSale,name="new"),
    path("editSale/<int:id>",sales.SaleClass.editSale,name="update"),
]