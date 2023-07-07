from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.TextField(default="")
    supplier = models.TextField(default="")
    imei = models.BigIntegerField(default=0)
    checked_in_person_name = models.TextField(default="")
    warranty_duration = models.TextField(default="")
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.product