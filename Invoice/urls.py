from django.urls import path
from Invoice import views as invoice


urlpatterns = [
    path("newInvoice",invoice.Invoices.newInvoice,name="new"),
    path("allInvoices",invoice.Invoices.getInvoices,name="all"),
    path("singleInvoice/<int:id>",invoice.Invoices.singleInvoice,name="single"),
]