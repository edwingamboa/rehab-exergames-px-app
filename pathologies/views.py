from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from utilities.constants import Constants
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView,
)
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import (
    Pathology,
)
from .forms import (
    PathologyCreationPopUpForm
)

class PathologyList(ListView):
    model = Pathology


class PathologyDetail(DetailView):
    model = Pathology


class PathologyCreation(CreateView):
    model = Pathology
    fields = ['name', 'code']
    success_msg = "Pathology " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('pathologies:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(PathologyCreation, self).form_valid(form)
    
    
class PathologyCreationPopUp(FormView):
    model = Pathology
    success_msg = "Pathology " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = PathologyCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class PathologyUpdate(UpdateView):
    model = Pathology
    fields = ['name', 'code']
    success_msg = "Pathology " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('pathologies:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(PathologyUpdate, self).form_valid(form)
