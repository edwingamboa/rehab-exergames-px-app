from django.db import models
from px_evaluation.models import (
    Instrument
)
from resources.models import Resource

from utilities.constants import Constants


class Measure(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.name


class Questionnaire(Instrument):
    evaluation_objective = models.TextField()
    target_respondents = models.TextField()
    questionnaire_document = models.ForeignKey(Resource)
    additional_documents = models.ManyToManyField(Resource)
    validity = models.CharField(max_length=140)
    validity_measure = models.ForeignKey(Measure)
    reliability = models.CharField(max_length=140)
    reliability_measure = models.ForeignKey(Measure)
    pre_testing_report = models.ForeignKey(Resource)
    status = models.CharField(
        max_length=20,
        default=Constants.INIT,
        choices=Constants.QUESTIONNAIRE_STATUS,
    )
