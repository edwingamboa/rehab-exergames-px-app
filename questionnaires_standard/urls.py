from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    MeasureCreation,
    MeasureDetail,
    MeasureList,
    MeasureUpdate,
    MeasureCreationPopUp,
    QuestionnaireDetail,
    QuestionnaireList,
    QuestionnaireCreation,
    QuestionnaireUpdate,
    QuestionnaireContinueCreation
)

urlpatterns = [
    url(r'^measures/$', MeasureList.as_view(), name='list_measures'),
    url(r'^measures/(?P<pk>\d+)$', MeasureDetail.as_view(), name='detail_measures'),
    url(r'^measures/new', MeasureCreation.as_view(), name='new_measures'),
    url(r'^measures/pop_up_new', MeasureCreationPopUp.as_view(), name='pop_up_new_measures'),
    url(r'^measures/update/(?P<pk>\d+)$', MeasureUpdate.as_view(), name='update_measures'),
    url(r'^questionnaire_dev/$', QuestionnaireList.as_view(), name='list'),
    url(r'^questionnaire_dev/(?P<pk>\d+)$', QuestionnaireDetail.as_view(), name='detail'),
    url(r'^questionnaire_dev/new', QuestionnaireCreation.as_view(), name='new'),
    url(r'^questionnaire_dev/update/(?P<pk>\d+)', QuestionnaireUpdate.as_view(), name='update'),
    url(r'^questionnaire_dev/continue/(?P<pk>\d+)', QuestionnaireContinueCreation.as_view(), name='continue'),
    url(r'^questionnaire_process',
        TemplateView.as_view(template_name='questionnaires_standard/questionnaire_process.html'),
        name='questionnaire_process'),
    url(r'^questionnaire_process/design',
        TemplateView.as_view(template_name='questionnaires_standard/questionnaire_design.html'),
        name='questionnaire_design'),
    url(r'^questionnaire_process/pre-testing',
        TemplateView.as_view(template_name='questionnaires_standard/questionnaire_pre_testing.html'),
        name='questionnaire_pre_testing'),
    url(r'^glossary',
        TemplateView.as_view(template_name='questionnaires_standard/glossary.html'),
        name='glossary'),
]