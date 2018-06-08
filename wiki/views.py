from .models import Definition
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView,
)
from django.http import HttpResponse
from .forms import (
    DefinitionForm,
    DefinitionCreationPopUpForm
)
from utilities.constants import Constants


# Create your views here.
class DefinitionList(ListView):
    model = Definition


class DefinitionDetail(DetailView):
    model = Definition


class DefinitionCreation(CreateView):
    model = Definition
    form_class = DefinitionForm
    success_msg = "Definition " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('wiki:detail_definitions', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(DefinitionCreation, self).form_valid(form)


class DefinitionUpdate(UpdateView):
    model = Definition
    form_class = DefinitionForm
    success_msg = "Definition " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('wiki:detail_definitions', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(DefinitionUpdate, self).form_valid(form)


class DefinitionCreationPopUp(FormView):
    model = Definition
    success_msg = "Definition " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = DefinitionCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class QuestionnaireProcess(TemplateView):
    template_name = 'wiki/questionnaire_dev/questionnaire_process.html'


class QuestionnaireDesign(TemplateView):
    template_name = 'wiki/questionnaire_dev/questionnaire_design.html'


class QuestionnairePreTesting(TemplateView):
    template_name = 'wiki/questionnaire_dev/questionnaire_pre_testing.html'
