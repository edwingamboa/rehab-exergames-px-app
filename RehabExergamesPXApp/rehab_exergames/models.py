import os
from django.db import models
from RehabExergamesPXApp.utilities.constants import Constants


def get_image_path(instance, filename):
    return os.path.join('games', str(instance.id), filename)


# Create your models here.
class ThematicContent(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()


class InteractionDevice(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    type = models.PositiveIntegerField(
        choices=Constants.DEVICE_TYPE
    )


class Game(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    status = models.PositiveIntegerField(
        default=Constants.ACTIVE,
        choices=Constants.GAME_STATUS
    )
    interaction_devices = models.ManyToManyField(InteractionDevice)

    @property
    def is_active(self):
        return self.estado == Constants.ACTIVE

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def __str__(self):
        return self.name