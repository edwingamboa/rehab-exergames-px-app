import os
from django.db import models
from resources.models import Resource
from rehab_exergames.models import (
    RehabilitationExergame,
    Constraint
)
from utilities.constants import Constants

def get_evaluation_file_path(instance, filename):
    return os.path.join('evaluation_files', str(instance.id), filename)

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


class PXEvaluation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    rehab_exergame_characterisation = models.ForeignKey(RehabilitationExergame, blank=True)
    players_characterisation = models.FileField(blank=True, upload_to=get_evaluation_file_path)
    rehabilitation_constraints = models.ManyToManyField(Constraint, blank=True)
    evaluation_goal = models.TextField()
    evaluation_aspects = models.ManyToManyField(Aspect, blank=True)
    evaluation_methods = models.ManyToManyField(Method, blank=True)
    evaluation_instruments = models.ManyToManyField(Instrument, blank=True)
    evaluation_plan = models.FileField(blank=True, upload_to=get_evaluation_file_path)
    evaluation_report = models.FileField(blank=True, upload_to=get_evaluation_file_path)
    current_stage = models.CharField(
        max_length=20,
        default=Constants.ENV_ANALYSIS,
        choices=Constants.EVALUATION_STAGE,
    )

    def __str__(self):
        return str(self.rehab_exergame_characterisation) + ':\n' + self.evaluation_goal