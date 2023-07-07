from django.db import models
from Stock.models import Stock

class Invoice(models.Model):
    document_number = receipt_number = models.CharField(max_length=5,null=True)
    supplier_name = models.TextField(default="")
    amount = models.IntegerField(default=0)
    number_of_devices = models.IntegerField(default=0)
    PO_box = models.TextField(default="")
    due_in_number_of_days = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    items = models.ManyToManyField(Stock)

    def __str__(self):
        return self.document_number

class InvoicePayments(models.Model):
    supplier_name = models.TextField(default="")
    payment_date = models.DateField(default="")
    pay_this_money_from = models.DateField(default="")
    payment_method = models.TextField(default="")
    cheque_no = models.IntegerField(default=0)
    invoice_date = models.DateField(default="")
    invoice_number = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)

    def __str__(self):
        return self.payment_date