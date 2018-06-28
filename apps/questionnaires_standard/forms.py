from django import forms
from django.forms import ModelForm
from .models import (
    Questionnaire,
    Measure
)
from apps.utilities.constants import Constants
from django.db.models import Q
from apps.utilities.custom_widgets import (
    RelatedFieldWidgetCanAdd,
    RelatedFieldWidgetCanAddMultiple
)
from apps.resources.models import Resource
from apps.px_evaluation.models import Aspect


class QuestionnaireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args,**kwargs)
        instance = kwargs.get('instance', None)
        if instance:
            self.fields['questionnaire_document'].queryset = Resource.objects.all()
            self.fields['additional_documents'].queryset = Resource.objects.all()
            self.fields['pre_testing_report'].queryset = Resource.objects.all()
            self.fields['aspects'].queryset = Aspect.objects.all()
            self.fields['validity_measure'].queryset = Measure.objects.filter(
                Q(type=Constants.VALIDITY)
            )
            self.fields['reliability_measure'].queryset = Measure.objects.filter(
                Q(type=Constants.RELIABILITY)
            )

    class Meta:
        model = Questionnaire
        fields = '__all__'
        exclude = ('status', 'methods', 'resources')
        widgets = {
            'questionnaire_document': RelatedFieldWidgetCanAdd(
                Resource,
                related_url='resources:pop_up_new'
            ),
            'validity_measure': RelatedFieldWidgetCanAdd(
                Measure,
                related_url='questionnaire:pop_up_new_measures'
            ),
            'reliability_measure': RelatedFieldWidgetCanAdd(
                Measure,
                related_url='questionnaire:pop_up_new_measures'
            ),
            'pre_testing_report': RelatedFieldWidgetCanAdd(
                Resource,
                related_url='resources:pop_up_new'
            ),
            'additional_documents': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
            ),
            'aspects': RelatedFieldWidgetCanAddMultiple(
                Aspect,
                related_url='px_evaluation:pop_up_new_aspects'
            ),
        }


class QuestionnaireContinueCreationForm(QuestionnaireForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireContinueCreationForm, self).__init__(*args,**kwargs)
        instance = kwargs.get('instance', None)
        if instance:
            if instance.status == Constants.INIT:
                del self.fields['description']
                del self.fields['target_respondents']
                del self.fields['aspects']
                del self.fields['questionnaire_document']
                del self.fields['additional_documents']
                del self.fields['validity']
                del self.fields['validity_measure']
                del self.fields['reliability']
                del self.fields['reliability_measure']
                del self.fields['pre_testing_report']
            elif instance.status == Constants.IN_DESIGN:
                del self.fields['name']
                del self.fields['target_respondents']
                del self.fields['aspects']
                del self.fields['evaluation_objective']
                del self.fields['validity']
                del self.fields['validity_measure']
                del self.fields['reliability']
                del self.fields['reliability_measure']
                del self.fields['pre_testing_report']
            elif instance.status == Constants.IN_PRE_TEST or instance.status == Constants.FINISHED:
                del self.fields['evaluation_objective']
                del self.fields['target_respondents']
                del self.fields['aspects']
                del self.fields['name']
                del self.fields['description']
                del self.fields['questionnaire_document']
                del self.fields['additional_documents']


class QuestionnaireUpdateForm(QuestionnaireForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireUpdateForm, self).__init__(*args,**kwargs)

        instance = kwargs.get('instance', None)
        if instance:
            if instance.status == Constants.INIT:
                del self.fields['description']
                del self.fields['questionnaire_document']
                del self.fields['additional_documents']
                del self.fields['validity']
                del self.fields['validity_measure']
                del self.fields['reliability']
                del self.fields['reliability_measure']
                del self.fields['pre_testing_report']
            elif instance.status == Constants.IN_DESIGN:
                del self.fields['validity']
                del self.fields['validity_measure']
                del self.fields['reliability']
                del self.fields['reliability_measure']
                del self.fields['pre_testing_report']


class MeasureForm(ModelForm):
    class Meta:
        model = Measure
        fields = '__all__'
        widgets = {
            'resources': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
            ),
        }


class MeasureCreationPopUpForm(ModelForm):
    class Meta:
        model = Measure
        fields = '__all__'
        exclude = ('resources',)
