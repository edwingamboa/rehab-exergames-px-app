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


class MovementList(ListView):
    model = Movement


class MovementDetail(DetailView):
    model = Movement


class MovementCreation(CreateView):
    model = Movement
    fields = ['name', 'description', 'configuration_parameters']
    success_msg = "Movement " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('movements:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MovementCreation, self).form_valid(form)


class MovementUpdate(UpdateView):
    model = Movement
    fields = ['name', 'description', 'configuration_parameters']
    success_msg = "Movement " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('movements:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MovementUpdate, self).form_valid(form)
