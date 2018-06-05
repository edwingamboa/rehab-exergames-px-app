from django import forms
from django.forms import ModelForm
from .models import (
    PXEvaluation,
    Aspect,
    Method,
    Instrument,
    MethodType,
)
from resources.models import Resource
from utilities.constants import Constants
from utilities.custom_widgets import (
    RelatedFieldWidgetCanAddMultiple,
    RelatedFieldWidgetCanAdd
)
from rehab_exergames.models import (
    RehabilitationExergame,
    Constraint,
)


class PXEvaluationForm(ModelForm):
    class Meta:
        model = PXEvaluation
        fields = '__all__'
        exclude = ('date', 'current_stage')
        widgets = {
            'rehab_exergame_characterisation': RelatedFieldWidgetCanAdd(
                RehabilitationExergame,
                related_url='rehab_exergames:pop_up_new'
            ),
            'rehabilitation_constraints': RelatedFieldWidgetCanAddMultiple(
                Constraint,
                related_url='rehab_exergames:pop_up_new_constraint'
            ),
            'resources': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
            ),
            'evaluation_aspects': RelatedFieldWidgetCanAddMultiple(
                Aspect,
                related_url='px_evaluation:pop_up_new_aspects'
            ),
            'evaluation_methods': RelatedFieldWidgetCanAddMultiple(
                Method,
                related_url='px_evaluation:pop_up_new_methods'
            ),
            'evaluation_instruments': RelatedFieldWidgetCanAddMultiple(
                Instrument,
                related_url='px_evaluation:pop_up_new_instruments'
            ),
        }


class PXEvaluationCreationForm(PXEvaluationForm):
    def __init__(self, *args, **kwargs):
        super(PXEvaluationCreationForm, self).__init__(*args, **kwargs)

        del self.fields['evaluation_goal']
        del self.fields['evaluation_aspects']
        del self.fields['evaluation_methods']
        del self.fields['evaluation_instruments']
        del self.fields['evaluation_plan']
        del self.fields['evaluation_report']


class PXEvaluationContinueForm(PXEvaluationForm):
    def __init__(self, *args, **kwargs):
        super(PXEvaluationContinueForm, self).__init__(*args, **kwargs)

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


class AspectForm(ModelForm):
    class Meta:
        model = Aspect
        fields = ['name', 'description', 'resources']
        widgets = {
            'resources': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
            ),
        }


class AspectCreationPopUpForm(ModelForm):
    class Meta:
        model = Aspect
        fields = ['name', 'description']


class MethodForm(ModelForm):
    class Meta:
        model = Method
        fields = ['name', 'description', 'type', 'resources']
        widgets = {
            'resources': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
            ),
            'type': RelatedFieldWidgetCanAdd(
                MethodType,
                related_url='px_evaluation:pop_up_new_method_types'
            ),
        }


class MethodCreationPopUpForm(ModelForm):
    class Meta:
        model = Method
        fields = ['name', 'description', 'type']


class MethodTypeCreationPopUpForm(ModelForm):
    class Meta:
        model = MethodType
        fields = '__all__'


class InstrumentCreationPopUpForm(ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'description', 'aspects', 'methods']


class InstrumentForm(ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'description', 'aspects', 'methods', 'resources']
        widgets = {
            'resources': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
            ),
            'aspects': RelatedFieldWidgetCanAddMultiple(
                Aspect,
                related_url='px_evaluation:pop_up_new_aspects'
            ),
            'methods': RelatedFieldWidgetCanAddMultiple(
                Method,
                related_url='px_evaluation:pop_up_new_methods'
            ),
        }
