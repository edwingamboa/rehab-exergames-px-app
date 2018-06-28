from django.forms import ModelForm
from .models import (
    Pathology
)


class PathologyCreationPopUpForm(ModelForm):
    class Meta:
        model = Pathology
        fields = '__all__'
