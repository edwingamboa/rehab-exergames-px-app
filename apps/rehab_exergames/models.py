import os
from django.db import models
from apps.utilities.constants import Constants
from apps.movements.models import Movement
from apps.interaction_devices.models import InteractionDevice
from apps.pathologies.models import Pathology


def get_image_path(instance, filename):
    return os.path.join('games', str(instance.id), filename)


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    status = models.PositiveIntegerField(
        default=Constants.ACTIVE,
        choices=Constants.GAME_STATUS
    )
    input_interaction_devices = models.ManyToManyField(InteractionDevice, related_name="input_devices")
    output_interaction_devices = models.ManyToManyField(InteractionDevice, related_name="output_devices")

    @property
    def is_active(self):
        return self.status == Constants.ACTIVE

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def __str__(self):
        return self.name


class Exergame (Game):
    thematic_content = models.PositiveIntegerField(
        choices=Constants.THEMATIC_CONTENT
    )
    associated_movements = models.ManyToManyField(Movement)
    configurable = models.BooleanField()
    provide_performance_assessment = models.BooleanField()


class RehabilitationTask (models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.name


class RehabilitationExergame (Exergame):
    rehabilitation_type = models.CharField(
        max_length=20,
        choices=Constants.REHABILITATION_TYPE
    )
    autonomy_degree = models.CharField(
        max_length=20,
        choices=Constants.AUTONOMY_DEGREE
    )
    associated_pathologies = models.ManyToManyField(Pathology, blank=True)
    assisted_rehabilitation_tasks = models.ManyToManyField(RehabilitationTask)


class ConstraintCategory (models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.name


class Constraint (models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    categories = models.ManyToManyField(ConstraintCategory)

    def __str__(self):
        return self.name