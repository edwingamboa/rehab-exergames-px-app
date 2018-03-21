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
    RehabilitationTask,
)


class RehabilitationTaskList(ListView):
    model = RehabilitationTask


class RehabilitationTaskDetail(DetailView):
    model = RehabilitationTask


class RehabilitationTaskCreation(CreateView):
    model = RehabilitationTask
    fields = ['name', 'description']
    success_msg = "Rehabilitation Task " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_task', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(RehabilitationTaskCreation, self).form_valid(form)


class RehabilitationTaskUpdate(UpdateView):
    model = RehabilitationTask
    fields = ['name', 'description']
    success_msg = "Rehabilitation Task " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_task', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(RehabilitationTaskUpdate, self).form_valid(form)