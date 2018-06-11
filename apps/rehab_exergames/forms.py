from django.forms import ModelForm
from .models import (
    RehabilitationExergame,
    Constraint,
    ConstraintCategory,
    RehabilitationTask,
)
from apps.movements.models import Movement
from apps.pathologies.models import Pathology
from apps.interaction_devices.models import InteractionDevice
from apps.utilities.constants import Constants
from django.db.models import Q
from apps.utilities.custom_widgets import (
    RelatedFieldWidgetCanAddMultiple
)


class RehabilitationExergameCreationPopUpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RehabilitationExergameCreationPopUpForm, self).__init__(*args, **kwargs)
        self.fields['input_interaction_devices'].queryset = InteractionDevice.objects.filter(
            Q(type=Constants.INPUT_DEVICE) | Q(type=Constants.IN_OUTPUT_DEVICE)
        )
        self.fields['output_interaction_devices'].queryset = InteractionDevice.objects.filter(
            Q(type=Constants.OUTPUT_DEVICE) | Q(type=Constants.IN_OUTPUT_DEVICE)
        )

    class Meta(object):
        model = RehabilitationExergame
        fields = '__all__'
        exclude = ['status']


class RehabilitationExergameForm(RehabilitationExergameCreationPopUpForm):
    class Meta(object):
        model = RehabilitationExergame
        fields = '__all__'
        exclude = ['status']
        widgets = {
            'input_interaction_devices': RelatedFieldWidgetCanAddMultiple(
                InteractionDevice,
                related_url='interaction_device:pop_up_new'
            ),
            'output_interaction_devices': RelatedFieldWidgetCanAddMultiple(
                InteractionDevice,
                related_url='interaction_device:pop_up_new'
            ),
            'associated_movements': RelatedFieldWidgetCanAddMultiple(
                Movement,
                related_url='movements:pop_up_new'
            ),
            'associated_pathologies': RelatedFieldWidgetCanAddMultiple(
                Pathology,
                related_url='pathologies:pop_up_new'
            ),
            'assisted_rehabilitation_tasks': RelatedFieldWidgetCanAddMultiple(
                RehabilitationTask,
                related_url='rehab_exergames:pop_up_new_task'
            ),
        }


class ConstraintForm(ModelForm):
    class Meta(object):
        model = Constraint
        fields = ['name', 'description', 'categories']
        widgets = {
            'categories': RelatedFieldWidgetCanAddMultiple(
                RehabilitationTask,
                related_url='rehab_exergames:pop_up_new_constraint_cat'
            ),
        }


class ConstraintCreationPopUpForm(ModelForm):
    class Meta(object):
        model = Constraint
        fields = ['name', 'description', 'categories']
        

class RehabilitationTaskCreationPopUpForm(ModelForm):
    class Meta:
        model = RehabilitationTask
        fields = '__all__'
        
        
class ConstraintCategoryCreationPopUpForm(ModelForm):
    class Meta:
        model = ConstraintCategory
        fields = '__all__'
