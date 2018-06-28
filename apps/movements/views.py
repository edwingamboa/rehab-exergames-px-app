from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from apps.utilities.constants import Constants
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView,
)
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import (
    Movement,
    ConfigurationParameter,
)
from .forms import (
    ConfigurationParameterCreationPopUpForm,
    MovementForm,
    MovementCreationPopUpForm,
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
    

class ConfigurationParameterCreationPopUp(FormView):
    model = ConfigurationParameter
    success_msg = "Configuration Parameter " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = ConfigurationParameterCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


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
    form_class = MovementForm
    success_msg = "Movement " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('movements:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MovementCreation, self).form_valid(form)


class MovementCreationPopUp(FormView):
    model = Movement
    success_msg = "Movement " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = MovementCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class MovementUpdate(UpdateView):
    model = Movement
    form_class = MovementForm
    success_msg = "Movement " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('movements:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MovementUpdate, self).form_valid(form)
