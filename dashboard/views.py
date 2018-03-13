# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView


# Create your views here.
class Dashboard(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome'] = 'Welcome'
        return context