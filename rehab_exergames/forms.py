from django import forms
from .models import RehabilitationExergame
from interaction_devices.models import InteractionDevice
from utilities.constants import Constants
from django.db.models import Q


class RehabilitationExergameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RehabilitationExergameForm, self).__init__(*args, **kwargs)
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
