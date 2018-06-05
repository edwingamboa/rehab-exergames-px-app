from django.forms import ModelForm
from .models import (
    DeviceTechnology,
    InteractionDevice
)
from utilities.custom_widgets import RelatedFieldWidgetCanAdd


class InteractionDeviceForm(ModelForm):
    class Meta:
        model = InteractionDevice
        fields = ['name', 'description', 'type', 'device_technology']
        widgets = {
            'device_technology': RelatedFieldWidgetCanAdd(
                DeviceTechnology,
                related_url='interaction_device:pop_up_new_tech'
            ),
        }


class InteractionDeviceCreationPopUpForm(ModelForm):
    class Meta:
        model = InteractionDevice
        fields = ['name', 'description', 'type', 'device_technology']


class DeviceTechnologyCreationPopUpForm(ModelForm):
    class Meta:
        model = DeviceTechnology
        fields = '__all__'
