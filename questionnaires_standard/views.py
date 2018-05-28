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
)
from .forms import QuestionnaireUpdateForm
from utilities.constants import Constants


# Create your views here.
class MeasureList(ListView):
    model = Measure


class MeasureDetail(DetailView):
    model = Measure


class MeasureCreation(CreateView):
    model = Measure
    fields = ['name', 'description', 'resources']
    success_msg = "Measure " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('questionnaires:detail_measures', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MeasureCreation, self).form_valid(form)


class MeasureUpdate(UpdateView):
    model = Measure
    fields = ['name', 'description', 'resources']
    success_msg = "Measure " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('questionnaires:detail_measures', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MeasureUpdate, self).form_valid(form)
    

class QuestionnaireList(ListView):
    model = Questionnaire

    
class QuestionnaireDetail(DetailView):
    model = Questionnaire


class QuestionnaireCreation(CreateView):
    model = Questionnaire
    fields = ['evaluation_objective', 'target_respondents', 'aspects']
    success_msg = "Evaluation " + Constants.SUCCESS_INIT_MESSAGE

    def get_success_url(self):
        return reverse_lazy('questionnaires:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(QuestionnaireCreation, self).form_valid(form)


class QuestionnaireContinueCreation(UpdateView):
    model = Questionnaire
    form_class = QuestionnaireUpdateForm
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
        print(form.data)
        if 'save_continue' in form.data:
            self.success_url = reverse_lazy('questionnaire:continue', kwargs={'pk': self.object.id})
        elif 'save' in form.data:
            self.success_url = reverse_lazy('questionnaire:detail', kwargs={'pk': self.object.id})
        return super(QuestionnaireContinueCreation, self).form_valid(form)


class QuestionnaireUpdate(UpdateView):
    model = Questionnaire
    fields = '__all__'
    exclude = ['status', 'methods', 'resources']
    template_name = 'questionnaires_standard/questionnaire_update.html'
    success_msg = "Questionnaire " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('questionnaire:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(QuestionnaireUpdate, self).form_valid(form)