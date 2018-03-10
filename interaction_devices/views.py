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
    InteractionDevice,
    DeviceTechnology,
)


# Create your views here
class InteractionDeviceList(ListView):
    model = InteractionDevice


class InteractionDeviceDetail(DetailView):
    model = InteractionDevice


class InteractionDeviceCreation(CreateView):
    model = InteractionDevice
    fields = ['name', 'description', 'type', 'device_technology']
    success_msg = "Interaction device " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('interaction_device:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(InteractionDeviceCreation, self).form_valid(form)

class InteractionDeviceUpdate(UpdateView):
    model = InteractionDevice
    fields = ['name', 'description', 'type', 'device_technology']
    success_msg = "Interaction device " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('interaction_device:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(InteractionDeviceUpdate, self).form_valid(form)

class DeviceTechnologyList(ListView):
    model = DeviceTechnology


class DeviceTechnologyDetail(DetailView):
    model = DeviceTechnology


class DeviceTechnologyCreation(CreateView):
    model = DeviceTechnology
    fields = ['name', 'description']
    success_msg = "Device technology " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('interaction_device:detail_tech', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(DeviceTechnologyCreation, self).form_valid(form)

class DeviceTechnologyUpdate(UpdateView):
    model = DeviceTechnology
    fields = ['name', 'description']
    success_msg = "Device technology " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('interaction_device:detail_tech', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(DeviceTechnologyUpdate, self).form_valid(form)
