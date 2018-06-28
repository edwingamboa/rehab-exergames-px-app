from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from apps.utilities.constants import Constants
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView,
)
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import (
    RehabilitationTask,
    RehabilitationExergame,
    ConstraintCategory,
    Constraint,
)
from .forms import (
    RehabilitationExergameForm,
    RehabilitationExergameCreationPopUpForm,
    ConstraintForm,
    ConstraintCreationPopUpForm,
    ConstraintCategoryCreationPopUpForm,
    RehabilitationTaskCreationPopUpForm,
)


class RehabilitationTaskList(ListView):
    model = RehabilitationTask


class RehabilitationTaskDetail(DetailView):
    model = RehabilitationTask


class RehabilitationTaskCreation(CreateView):
    model = RehabilitationTask
    fields = ['name', 'description']
    success_msg = "Rehabilitation Task " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_task', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(RehabilitationTaskCreation, self).form_valid(form)


class RehabilitationTaskCreationPopUp(FormView):
    model = RehabilitationTask
    success_msg = "Rehabilitation Task " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = RehabilitationTaskCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class RehabilitationTaskUpdate(UpdateView):
    model = RehabilitationTask
    fields = ['name', 'description']
    success_msg = "Rehabilitation Task " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_task', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(RehabilitationTaskUpdate, self).form_valid(form)


class RehabilitationExergameList(ListView):
    model = RehabilitationExergame


class RehabilitationExergameDetail(DetailView):
    model = RehabilitationExergame


class RehabilitationExergameCreation(CreateView):
    model = RehabilitationExergame
    form_class = RehabilitationExergameForm
    success_msg = "Rehabilitation Exergame " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(RehabilitationExergameCreation, self).form_valid(form)


class RehabilitationExergameCreationPopUp(FormView):
    model = RehabilitationExergame
    success_msg = "Rehabilitation Exergame " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = RehabilitationExergameCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class RehabilitationExergameUpdate(UpdateView):
    model = RehabilitationExergame
    form_class = RehabilitationExergameForm
    success_msg = "Rehabilitation Exergame " + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(RehabilitationExergameUpdate, self).form_valid(form)


class ConstraintCategoryList(ListView):
    model = ConstraintCategory


class ConstraintCategoryDetail(DetailView):
    model = ConstraintCategory


class ConstraintCategoryCreation(CreateView):
    model = ConstraintCategory
    fields = ['name', 'description']
    success_msg = "Constraint Category " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_constraint_cat', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ConstraintCategoryCreation, self).form_valid(form)
    
    
class ConstraintCategoryCreationPopUp(FormView):
    model = ConstraintCategory
    success_msg = "Constraint Category " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = ConstraintCategoryCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class ConstraintCategoryUpdate(UpdateView):
    model = ConstraintCategory
    fields = ['name', 'description']
    success_msg = "Constraint Category" + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_constraint_cat', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ConstraintCategoryUpdate, self).form_valid(form)


class ConstraintList(ListView):
    template_name = 'rehab_exergames/constraint_list.html'
    model = ConstraintCategory


class ConstraintFilteredByCategoryList(ListView):
    model = Constraint
    template_name = 'rehab_exergames/constraintfilteredbycategory_list.html'

    def get_queryset(self):
        category = ConstraintCategory.objects.get(id=self.kwargs['pk'])
        print(category)
        return Constraint.objects.filter(categories__id=category.id)


class ConstraintDetail(DetailView):
    model = Constraint


class ConstraintCreation(CreateView):
    model = Constraint
    form_class = ConstraintForm
    success_msg = "Constraint " + Constants.SUCCESS_CREATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_constraint', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ConstraintCreation, self).form_valid(form)


class ConstraintCreationPopUp(FormView):
    model = Constraint
    success_msg = "Constraint " + Constants.SUCCESS_CREATE_MESSAGE
    template_name = 'form_popup.html'
    form_class = ConstraintCreationPopUpForm

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        object = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s");</script>' % (object.pk, object))


class ConstraintUpdate(UpdateView):
    model = Constraint
    form_class = ConstraintForm
    success_msg = "Constraint" + Constants.SUCCESS_UPDATE_MESSAGE

    def get_success_url(self):
        return reverse_lazy('rehab_exergames:detail_constraint', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(ConstraintUpdate, self).form_valid(form)