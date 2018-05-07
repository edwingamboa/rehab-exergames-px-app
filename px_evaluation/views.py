from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from .models import (
    Aspect,
    Method,
    MethodType
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from utilities.constants import Constants


class AspectList(ListView):
    model = Aspect


class AspectDetail(DetailView):
    model = Aspect


class AspectCreation(CreateView):
    model = Aspect
    fields = ['name', 'description', 'resources']
    success_msg = "Aspect " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_aspects', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(AspectCreation, self).form_valid(form)


class AspectUpdate(UpdateView):
    model = Aspect
    fields = ['name', 'description', 'resources']
    success_msg = "Aspect " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_aspects', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(AspectUpdate, self).form_valid(form)


class MethodList(ListView):
    model = Method


class MethodDetail(DetailView):
    model = Method


class MethodCreation(CreateView):
    model = Method
    fields = ['name', 'description', 'type', 'resources']
    success_msg = "Method " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_methods', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MethodCreation, self).form_valid(form)


class MethodUpdate(UpdateView):
    model = Method
    fields = ['name', 'description', 'type', 'resources']
    success_msg = "Method " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_methods', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MethodUpdate, self).form_valid(form)

    
class MethodTypeList(ListView):
    model = MethodType


class MethodTypeDetail(DetailView):
    model = MethodType


class MethodTypeCreation(CreateView):
    model = MethodType
    fields = ['name', 'description']
    success_msg = "Method Type " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_method_types', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MethodTypeCreation, self).form_valid(form)


class MethodTypeUpdate(UpdateView):
    model = MethodType
    fields = ['name', 'description']
    success_msg = "Method Type " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_method_types', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MethodTypeUpdate, self).form_valid(form)