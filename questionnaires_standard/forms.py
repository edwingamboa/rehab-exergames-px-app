from django import forms
from .models import Questionnaire
from utilities.constants import Constants


class QuestionnaireUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireUpdateForm, self).__init__(*args,**kwargs)

        instance = kwargs.get('instance', None)
        if instance:
            if instance.status == Constants.INIT:
                del self.fields['name']
                del self.fields['description']
                del self.fields['questionnaire_document']
                del self.fields['additional_documents']
                del self.fields['validity']
                del self.fields['validity_measure']
                del self.fields['reliability']
                del self.fields['reliability_measure']
                del self.fields['pre_testing_report']
            elif instance.status == Constants.IN_DESIGN:
                del self.fields['evaluation_objective']
                del self.fields['target_respondents']
                del self.fields['aspects']
                del self.fields['validity']
                del self.fields['validity_measure']
                del self.fields['reliability']
                del self.fields['reliability_measure']
                del self.fields['pre_testing_report']
            elif instance.status == Constants.IN_PRE_TEST:
                del self.fields['evaluation_objective']
                del self.fields['target_respondents']
                del self.fields['aspects']
                del self.fields['name']
                del self.fields['description']
                del self.fields['questionnaire_document']
                del self.fields['additional_documents']

    class Meta:
        model = Questionnaire
        fields = '__all__'
        exclude = ('status', 'methods', 'resources')