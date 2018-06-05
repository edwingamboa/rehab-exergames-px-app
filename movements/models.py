from django.db import models


# Create your models here.
class ConfigurationParameter (models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.name


class Movement (models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    configuration_parameters = models.ManyToManyField(ConfigurationParameter, blank=True)

    def __str__(self):
        return self.name
