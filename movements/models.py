from django.db import models


# Create your models here.
class ConfigurationParameter (models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()


class Movement (models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    configuration_parameters = models.ManyToManyField(ConfigurationParameter, blank=True)