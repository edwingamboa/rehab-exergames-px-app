from django.shortcuts import render
from RehabExergamesPXApp.utilities.constants import Constants
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import (
    InteractionDevice
)


# Create your views here
class InteractionDeviceList(ListView):
    model = InteractionDevice


class InteractionDeviceDetail(DetailView):
    model = InteractionDevice


class InteractionDeviceCreation(CreateView):
    model = InteractionDevice
    success_msg = "Interaction device " +

class InteractionDeviceUpdate(UpdateView):
    model = InteractionDevice
