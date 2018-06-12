# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from apps.px_evaluation.models import PXEvaluation
from apps.rehab_exergames.models import (
    RehabilitationExergame,
    Constraint
)
from apps.questionnaires_standard.models import Questionnaire


# Create your views here.
class Dashboard(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['px_evaluations'] = PXEvaluation.objects.order_by('-date')[:5]
        context['rehab_exergames'] = RehabilitationExergame.objects.order_by('-id')[:5]
        context['total_px_evaluations'] = len(PXEvaluation.objects.all())
        context['total_rehab_exergames'] = len(RehabilitationExergame.objects.all())
        context['total_constraints'] = len(Constraint.objects.all())
        context['total_questionnaires'] = len(Questionnaire.objects.all())
        return context
