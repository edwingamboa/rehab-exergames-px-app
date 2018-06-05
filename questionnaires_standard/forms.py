from django import forms
from .models import (
    Questionnaire,
    Measure
)
from utilities.constants import Constants
from django.db.models import Q
from utilities.custom_widgets import (
    RelatedFieldWidgetCanAdd,
    RelatedFieldWidgetCanAddMultiple
)
from resources.models import Resource
from px_evaluation.models import Aspect


class QuestionnaireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args,**kwargs)
        instance = kwargs.get('instance', None)
        if instance:
            self.fields['questionnaire_document'].queryset = Resource.objects.all()
            self.fields['additional_documents'].queryset = Resource.objects.all()
            self.fields['pre_testing_report'].queryset = Resource.objects.all()
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
            'pre_testing_report': RelatedFieldWidgetCanAdd(
                Resource,
                related_url='resources:pop_up_new'
            ),
            'additional_documents': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
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