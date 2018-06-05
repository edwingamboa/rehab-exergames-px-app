from django import forms
from django.forms import ModelForm
from .models import (
    PXEvaluation,
    Aspect
)
from utilities.constants import Constants


class PXEvaluationUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PXEvaluationUpdateForm, self).__init__(*args,**kwargs)

        instance = kwargs.get('instance', None)
        if instance:
            if instance.current_stage == Constants.ENV_ANALYSIS:
                del self.fields['evaluation_goal']
                del self.fields['evaluation_aspects']
                del self.fields['evaluation_methods']
                del self.fields['evaluation_instruments']
                del self.fields['evaluation_plan']
                del self.fields['evaluation_report']
            elif instance.current_stage == Constants.EVAL_GOAL_DEF:
                del self.fields['rehab_exergame_characterisation']
                del self.fields['players_characterisation']
                del self.fields['rehabilitation_constraints']
                del self.fields['evaluation_aspects']
                del self.fields['evaluation_methods']
                del self.fields['evaluation_instruments']
                del self.fields['evaluation_plan']
                del self.fields['evaluation_report']
            elif instance.current_stage == Constants.ASPECTS_SEL:
                del self.fields['rehab_exergame_characterisation']
                del self.fields['players_characterisation']
                del self.fields['rehabilitation_constraints']
                del self.fields['evaluation_goal']
                del self.fields['evaluation_methods']
                del self.fields['evaluation_instruments']
                del self.fields['evaluation_plan']
                del self.fields['evaluation_report']
            elif instance.current_stage == Constants.METHODS_SEL:
                del self.fields['rehab_exergame_characterisation']
                del self.fields['players_characterisation']
                del self.fields['rehabilitation_constraints']
                del self.fields['evaluation_goal']
                del self.fields['evaluation_aspects']
                del self.fields['evaluation_instruments']
                del self.fields['evaluation_plan']
                del self.fields['evaluation_report']
            elif instance.current_stage == Constants.INSTRUMENTS_SEL:
                del self.fields['rehab_exergame_characterisation']
                del self.fields['players_characterisation']
                del self.fields['rehabilitation_constraints']
                del self.fields['evaluation_goal']
                del self.fields['evaluation_aspects']
                del self.fields['evaluation_methods']
                del self.fields['evaluation_plan']
                del self.fields['evaluation_report']
            elif instance.current_stage == Constants.EVAL_PREP:
                del self.fields['rehab_exergame_characterisation']
                del self.fields['players_characterisation']
                del self.fields['rehabilitation_constraints']
                del self.fields['evaluation_goal']
                del self.fields['evaluation_aspects']
                del self.fields['evaluation_methods']
                del self.fields['evaluation_instruments']
                del self.fields['evaluation_report']
            elif instance.current_stage == Constants.EVAL or instance.current_stage == Constants.REPORT:
                del self.fields['rehab_exergame_characterisation']
                del self.fields['players_characterisation']
                del self.fields['rehabilitation_constraints']
                del self.fields['evaluation_goal']
                del self.fields['evaluation_aspects']
                del self.fields['evaluation_methods']
                del self.fields['evaluation_instruments']
                del self.fields['evaluation_plan']

    class Meta:
        model = PXEvaluation
        fields = '__all__'
        exclude = ('date', 'current_stage')


class AspectForm(ModelForm):
    class Meta:
        model = Aspect
        fields = ['name', 'description', 'resources']


class AspectCreationPopUpForm(ModelForm):
    class Meta:
        model = Aspect
        fields = ['name', 'description']