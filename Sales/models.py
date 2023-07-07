from django.db import models

class Sale(models.Model):
    product = models.TextField(default="")
    supplier = models.TextField(default="")
    imei = models.BigIntegerField(default=0)
    picked_at_shop = models.BooleanField(default=False)
    delivered_to_client_by = models.TextField(default="")
    client_name = models.TextField(default="")
    client_phone_number = models.IntegerField(default=0)
    client_email = models.EmailField(default="")
    client_location = models.TextField(default="")
    client_pin = models.TextField(default="")
    sold_by = models.TextField(default="")
    status = models.TextField(default="")
    warranty_status = models.TextField(default="")
    cash = models.IntegerField(default=0)
    mpesa = models.IntegerField(default=0)
    invoiced_amount = models.IntegerField(default=0)
    expense_name = models.TextField(default="")
    expense_amount = models.IntegerField(default=0)

    def __str__(self):
       return self.product
    
