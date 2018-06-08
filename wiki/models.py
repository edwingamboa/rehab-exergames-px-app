from django.db import models
from resources.models import Resource


# Create your models here.
class Definition(models.Model):
    term = models.CharField(max_length=140)
    definition = models.TextField()
    acronym = models.CharField(max_length=20, blank=True)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.term
