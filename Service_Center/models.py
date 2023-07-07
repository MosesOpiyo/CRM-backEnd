from django.db import models

from Stock.models import Stock

class Comment(models.Model):
    comment = models.TextField(default="")

    def __str__(self):
        return str(self.id)

class Device(models.Model):
    device = models.ForeignKey(Stock,on_delete=models.CASCADE)
    user_damage = models.TextField(default="")
    user_damage_comment = models.TextField(default="")
    amount = models.IntegerField(default=0)
    taken_by = models.TextField(default="")
    taken_date = models.TextField(default="")
    comment = models.ManyToManyField(Comment)
    issue = models.TextField(default="")
    service_center_feedback = models.TextField(default="")
    status = models.TextField(default="")

    def __str__(self):
        return self.device.product

class Service_Center(models.Model):
    service_center_name = models.TextField(default="")
    devices = models.ManyToManyField(Device)

    def __str__(self):
        return self.service_center_name

