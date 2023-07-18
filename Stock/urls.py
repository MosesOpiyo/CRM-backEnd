from django.urls import path
import Stock.views as stock

urlpatterns = [
    path("AllStocks",stock.stockClass.allStocks,name="all"),
    path("SingleStock/<int:id>",stock.stockClass.singleStock,name="stock"),
    path("postStocks",stock.stockClass.postStock,name="new_stock"),
    path("editStock/<int:id>",stock.stockClass.editStock,name="update"),
    path("AllStockValue",stock.stockClass.allStockValue,name="allValue"),
]