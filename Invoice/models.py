from django.db import models
from Stock.models import Stock
import os,binascii

class Invoice(models.Model):
    document_number = models.CharField(max_length=5,default="")
    supplier_name = models.TextField(default="")
    amount = models.IntegerField(default=0)
    number_of_devices = models.IntegerField(default=0)
    PO_number = models.IntegerField(default=0)
    due_date = models.DateField(default="")
    balance = models.IntegerField(default=0)
    payment_date = models.DateField(auto_now_add=True)
    pay_this_money_from = models.DateField(default="")
    payment_method = models.TextField(default="")
    cheque_no_or_ref = models.IntegerField(default=0)
    invoice_date = models.DateField(default="")
    invoice_number = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    items = models.ManyToManyField(Stock)

    def __str__(self):
        return self.document_number
    
    def save(self, *args, **kwargs):
        if not self.document_number:
            self.document_number = self.generate_number()
        return super().save(*args, **kwargs)
 
    
    @classmethod
    def generate_number(cls):
        return binascii.hexlify(os.urandom(6)).decode()
