from django.db import models
from resources.models import Resource


class Aspect(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    resources = models.ManyToManyField(Resource, blank=True)
