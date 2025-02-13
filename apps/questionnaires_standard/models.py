from django.db import models
from apps.px_evaluation.models import (
    Instrument
)
from apps.resources.models import Resource

from apps.utilities.constants import Constants


class Measure(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    type = models.CharField(
        max_length=20,
        choices=Constants.QUESTIONNAIRE_MEASURE_TYPES,
    )
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.name


class Questionnaire(Instrument):
    evaluation_objective = models.TextField()
    target_respondents = models.TextField()
    questionnaire_document = models.ForeignKey(Resource, related_name='%(class)s_questionnaire_doc', null=True)
    additional_documents = models.ManyToManyField(Resource, related_name='%(class)s_additional_docs', null=True)
    validity = models.CharField(max_length=140)
    validity_measure = models.ForeignKey(Measure, related_name='%(class)s_validity', null=True)
    reliability = models.CharField(max_length=140)
    reliability_measure = models.ForeignKey(Measure, related_name='%(class)s_reliability', null=True)
    pre_testing_report = models.ForeignKey(Resource, related_name='%(class)s_pre_test_report', null=True)
    status = models.CharField(
        max_length=20,
        default=Constants.INIT,
        choices=Constants.QUESTIONNAIRE_STATUS,
    )
