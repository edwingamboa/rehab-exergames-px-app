from django.forms import ModelForm
from .models import (
    ConfigurationParameter,
    Movement
)
from utilities.custom_widgets import RelatedFieldWidgetCanAddMultiple


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


class ConfigurationParameterCreationPopUpForm(ModelForm):
    class Meta:
        model = ConfigurationParameter
        fields = '__all__'
