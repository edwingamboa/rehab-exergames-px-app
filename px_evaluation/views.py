from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from .models import (
    Aspect,
    Method,
    MethodType,
    Instrument,
    PXEvaluation,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from utilities.constants import Constants
from .forms import PXEvaluationUpdateForm


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


class InstrumentList(ListView):
    model = Instrument


class InstrumentDetail(DetailView):
    model = Instrument


class InstrumentCreation(CreateView):
    model = Instrument
    fields = ['name', 'description', 'aspects', 'methods', 'resources']
    success_msg = "Instrument " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_instruments', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(InstrumentCreation, self).form_valid(form)


class InstrumentUpdate(UpdateView):
    model = Instrument
    fields = ['name', 'description', 'aspects', 'methods', 'resources']
    success_msg = "Instrument " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail_instruments', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(InstrumentUpdate, self).form_valid(form)


class PXEvaluationList(ListView):
    model = PXEvaluation


class PXEvaluationDetail(DetailView):
    model = PXEvaluation


class PXEvaluationCreation(CreateView):
    model = PXEvaluation
    fields = ['rehab_exergame_characterisation', 'players_characterisation', 'rehabilitation_constraints']
    success_msg = "Evaluation " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('px_evaluation:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(PXEvaluationCreation, self).form_valid(form)


class PXEvaluationUpdate(UpdateView):
    model = PXEvaluation
    form_class = PXEvaluationUpdateForm
    success_msg = "Evaluation " + Constants.SUCCESS_CREATE_MESSAGE

    def form_valid(self, form):
        px_evaluation = form.save(commit=False)
        if px_evaluation.current_stage == Constants.ENV_ANALYSIS:
            px_evaluation.current_stage = Constants.EVAL_GOAL_DEF
        elif px_evaluation.current_stage == Constants.EVAL_GOAL_DEF:
            px_evaluation.current_stage = Constants.ASPECTS_SEL
        elif px_evaluation.current_stage == Constants.ASPECTS_SEL:
            px_evaluation.current_stage = Constants.METHODS_SEL
        elif px_evaluation.current_stage == Constants.METHODS_SEL:
            px_evaluation.current_stage = Constants.INSTRUMENTS_SEL
        elif px_evaluation.current_stage == Constants.INSTRUMENTS_SEL:
            px_evaluation.current_stage = Constants.EVAL_PREP
        elif px_evaluation.current_stage == Constants.EVAL_PREP:
            px_evaluation.current_stage = Constants.REPORT

        px_evaluation.save()
        messages.success(self.request, self.success_msg)
        print(form.data)
        if 'save_continue' in form.data:
            self.success_url = reverse_lazy('px_evaluation:update', kwargs={'pk': self.object.id})
        elif 'save' in form.data:
            self.success_url = reverse_lazy('px_evaluation:detail', kwargs={'pk': self.object.id})
        return super(PXEvaluationUpdate, self).form_valid(form)
