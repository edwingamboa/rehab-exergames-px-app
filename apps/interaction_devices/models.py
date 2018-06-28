import os
from django.db import models
from apps.utilities.constants import Constants


class DeviceTechnology(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.name


class InteractionDevice(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    device_technology = models.ForeignKey(DeviceTechnology,blank=True, null=True)
    type = models.PositiveIntegerField(
        choices=Constants.DEVICE_TYPE
    )

    def __str__(self):
        return self.name
