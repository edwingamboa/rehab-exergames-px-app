from django.forms import ModelForm
from .models import (
    Definition,
)
from apps.resources.models import Resource
from apps.utilities.custom_widgets import (
    RelatedFieldWidgetCanAddMultiple,
)

class DefinitionForm(ModelForm):
    class Meta:
        model = Definition
        fields = '__all__'
        widgets = {
            'resources': RelatedFieldWidgetCanAddMultiple(
                Resource,
                related_url='resources:pop_up_new'
            ),
        }


class DefinitionCreationPopUpForm(ModelForm):
    class Meta:
        model = Definition
        fields = '__all__'

