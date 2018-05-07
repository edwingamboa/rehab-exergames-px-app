from django.db import models
from resources.models import Resource


class Aspect(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.name


class MethodType(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Method(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    type = models.ForeignKey(MethodType)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    aspects = models.ManyToManyField(Aspect, blank=True)
    methods = models.ManyToManyField(Method, blank=True)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.name
