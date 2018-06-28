from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from .models import (
    Measure,
    Questionnaire
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView,
)
from django.http import HttpResponse
from .forms import (
    QuestionnaireContinueCreationForm,
    QuestionnaireUpdateForm,
    MeasureForm,
    MeasureCreationPopUpForm,
)
from apps.utilities.constants import Constants
from django.views.generic import TemplateView


# Create your views here.
class MeasureList(ListView):
    model = Measure


class MeasureDetail(DetailView):
    model = Measure


class MeasureCreation(CreateView):
    model = Measure
    success_msg = "Measure " + Constants.SUCCESS_CREATE_MESSAGE
    form_class = MeasureForm

    def get_success_url(self):
        return reverse_lazy('questionnaire:detail_measures', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MeasureCreation, self).form_valid(form)


class MeasureCreationPopUp(FormView):
    model = Measure
    success_msg = "Measure " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = MeasureCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class MeasureUpdate(UpdateView):
    model = Measure
    success_msg = "Measure " + Constants.SUCCESS_UPDATE_MESSAGE
    form_class = MeasureForm

    def get_success_url(self):
        return reverse_lazy('questionnaire:detail_measures', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MeasureUpdate, self).form_valid(form)
    

class QuestionnaireList(ListView):
    model = Questionnaire

    
class QuestionnaireDetail(DetailView):
    model = Questionnaire


class InitQuestionnaireCreation(TemplateView):
    template_name = 'questionnaires_standard/questionnaire_pre_form.html'


class QuestionnaireCreation(CreateView):
    model = Questionnaire
    fields = ['evaluation_objective', 'name', 'aspects', 'target_respondents']
    success_msg = "Evaluation " + Constants.SUCCESS_INIT_MESSAGE

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        questionnaire = form.save(commit=False)
        questionnaire.status = Constants.IN_DESIGN
        questionnaire.save()
        if 'save_continue' in form.data:
            self.success_url = reverse_lazy('questionnaire:continue', kwargs={'pk': questionnaire.id})
        elif 'save' in form.data:
            self.success_url = reverse_lazy('questionnaire:detail', kwargs={'pk': questionnaire.id})
        return super(QuestionnaireCreation, self).form_valid(form)


class QuestionnaireContinueCreation(UpdateView):
    model = Questionnaire
    form_class = QuestionnaireContinueCreationForm
    success_msg = "Questionnaire " + Constants.SUCCESS_CONTINUE_MESSAGE

    def form_valid(self, form):
        questionnaire_dev = form.save(commit=False)
        if questionnaire_dev.status == Constants.INIT:
            questionnaire_dev.status = Constants.IN_DESIGN
        elif questionnaire_dev.status == Constants.IN_DESIGN:
            questionnaire_dev.status = Constants.IN_PRE_TEST
        elif questionnaire_dev.status == Constants.IN_PRE_TEST:
            questionnaire_dev.status = Constants.FINISHED

        questionnaire_dev.save()
        messages.success(self.request, self.success_msg)
        if 'save_continue' in form.data:
            self.success_url = reverse_lazy('questionnaire:continue', kwargs={'pk': self.object.id})
        elif 'save' in form.data:
            self.success_url = reverse_lazy('questionnaire:detail', kwargs={'pk': self.object.id})
        return super(QuestionnaireContinueCreation, self).form_valid(form)


class QuestionnaireUpdate(UpdateView):
    model = Questionnaire
    form_class = QuestionnaireUpdateForm
    template_name = 'questionnaires_standard/questionnaire_update.html'
    success_msg = "Questionnaire " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('questionnaire:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(QuestionnaireUpdate, self).form_valid(form)
