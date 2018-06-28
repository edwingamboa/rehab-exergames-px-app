from django.forms import ModelForm
from .models import (
    ConfigurationParameter,
    Movement
)
from apps.utilities.custom_widgets import RelatedFieldWidgetCanAddMultiple


class MovementForm(ModelForm):
    class Meta:
        model = Movement
        fields = ['name', 'description', 'configuration_parameters']
        widgets = {
            'configuration_parameters': RelatedFieldWidgetCanAddMultiple(
                ConfigurationParameter,
                related_url='movements:pop_up_new_config_par'
            ),
        }


class MovementCreationPopUpForm(ModelForm):
    class Meta:
        model = Movement
        fields = ['name', 'description', 'configuration_parameters']


class ConfigurationParameterCreationPopUpForm(ModelForm):
    class Meta:
        model = ConfigurationParameter
        fields = '__all__'
