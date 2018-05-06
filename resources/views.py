from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from .models import Resource
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from utilities.constants import Constants


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


class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['name', 'description', 'url', 'file']
    success_msg = "Resource " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('resources:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ResourceUpdate, self).form_valid(form)
