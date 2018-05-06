import os
from django.db import models


def get_resource_path(instance, filename):
    return os.path.join('resources', str(instance.id), filename)

class Resource(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    url = models.URLField(blank=True)
    file = models.FileField(blank=True, upload_to=get_resource_path)
