from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from utilities.constants import Constants
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import (
    Movement,
    ConfigurationParameter,
)


class ConfigurationParameterList(ListView):
    model = ConfigurationParameter


class ConfigurationParameterDetail(DetailView):
    model = ConfigurationParameter


class ConfigurationParameterCreation(CreateView):
    model = ConfigurationParameter
    fields = ['name', 'description']
    success_msg = "Configuration parameter " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('movements:detail_config_par', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ConfigurationParameterCreation, self).form_valid(form)


class ConfigurationParameterUpdate(UpdateView):
    model = ConfigurationParameter
    fields = ['name', 'description']
    success_msg = "Configuration parameter " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('movements:detail_config_par', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ConfigurationParameterUpdate, self).form_valid(form)
