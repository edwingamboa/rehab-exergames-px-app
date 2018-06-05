from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from utilities.constants import Constants
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView,
)
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import (
    InteractionDevice,
    DeviceTechnology,
)
from .forms import (
    DeviceTechnologyCreationPopUpForm,
    InteractionDeviceForm,
    InteractionDeviceCreationPopUpForm
)


# Create your views here
class InteractionDeviceList(ListView):
    model = InteractionDevice


class InteractionDeviceDetail(DetailView):
    model = InteractionDevice


class InteractionDeviceCreation(CreateView):
    model = InteractionDevice
    form_class = InteractionDeviceForm
    success_msg = "Interaction device " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('interaction_device:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(InteractionDeviceCreation, self).form_valid(form)


class InteractionDeviceCreationPopUp(FormView):
    model = InteractionDevice
    success_msg = "Interaction Device " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = InteractionDeviceCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class InteractionDeviceUpdate(UpdateView):
    model = InteractionDevice
    form_class = InteractionDeviceForm
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


class DeviceTechnologyCreationPopUp(FormView):
    model = DeviceTechnology
    success_msg = "Device Technology " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = DeviceTechnologyCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class DeviceTechnologyUpdate(UpdateView):
    model = DeviceTechnology
    fields = ['name', 'description']
    success_msg = "Device technology " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('interaction_device:detail_tech', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(DeviceTechnologyUpdate, self).form_valid(form)
