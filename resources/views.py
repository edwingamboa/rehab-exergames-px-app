from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from .models import Resource
from .forms import ResourceForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView
)
from utilities.constants import Constants
from django.http import HttpResponse


class ResourceList(ListView):
    model = Resource


class ResourceDetail(DetailView):
    model = Resource


class ResourceCreation(CreateView):
    model = Resource
    fields = ['name', 'description', 'url', 'file']
    success_msg = "Resource " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('resources:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ResourceCreation, self).form_valid(form)


class ResourceCreationPopUp(FormView):
    model = Resource
    success_msg = "Resource " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'

    form_class = ResourceForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['name', 'description', 'url', 'file']
    success_msg = "Resource " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('resources:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ResourceUpdate, self).form_valid(form)
