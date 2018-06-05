from django.conf.urls import url

from .views import (
    AspectCreation,
    AspectDetail,
    AspectList,
    AspectUpdate,
    AspectCreationPopUp,
    MethodCreation,
    MethodDetail,
    MethodList,
    MethodUpdate,
    MethodCreationPopUp,
    MethodTypeCreation,
    MethodTypeDetail,
    MethodTypeList,
    MethodTypeUpdate,
    MethodTypeCreationPopUp,
    InstrumentCreation,
    InstrumentDetail,
    InstrumentList,
    InstrumentUpdate,
    InstrumentCreationPopUp,
    PXEvaluationDetail,
    PXEvaluationList,
    PXEvaluationCreation,
    PXEvaluationUpdate,
    PXEvaluationContinueCreation
)

urlpatterns = [
    url(r'^aspects/$', AspectList.as_view(), name='list_aspects'),
    url(r'^aspects/(?P<pk>\d+)$', AspectDetail.as_view(), name='detail_aspects'),
    url(r'^aspects/new', AspectCreation.as_view(), name='new_aspects'),
    url(r'^aspects/update/(?P<pk>\d+)$', AspectUpdate.as_view(), name='update_aspects'),
    url(r'^aspects/pop_up_new', AspectCreationPopUp.as_view(), name='pop_up_new_aspects'),
    url(r'^methods/$', MethodList.as_view(), name='list_methods'),
    url(r'^methods/(?P<pk>\d+)$', MethodDetail.as_view(), name='detail_methods'),
    url(r'^methods/new', MethodCreation.as_view(), name='new_methods'),
    url(r'^methods/pop_up_new', MethodCreationPopUp.as_view(), name='pop_up_new_methods'),
    url(r'^methods/update/(?P<pk>\d+)$', MethodUpdate.as_view(), name='update_methods'),
    url(r'^method_types/$', MethodTypeList.as_view(), name='list_method_types'),
    url(r'^method_types/(?P<pk>\d+)$', MethodTypeDetail.as_view(), name='detail_method_types'),
    url(r'^method_types/new', MethodTypeCreation.as_view(), name='new_method_types'),
    url(r'^method_types/pop_up_new', MethodTypeCreationPopUp.as_view(), name='pop_up_new_method_types'),
    url(r'^method_types/update/(?P<pk>\d+)$', MethodTypeUpdate.as_view(), name='update_method_types'),
    url(r'^instruments/$', InstrumentList.as_view(), name='list_instruments'),
    url(r'^instruments/(?P<pk>\d+)$', InstrumentDetail.as_view(), name='detail_instruments'),
    url(r'^instruments/new', InstrumentCreation.as_view(), name='new_instruments'),
    url(r'^instruments/pop_up_new', InstrumentCreationPopUp.as_view(), name='pop_up_new_instruments'),
    url(r'^instruments/update/(?P<pk>\d+)$', InstrumentUpdate.as_view(), name='update_instruments'),
    url(r'^px_evaluations/$', PXEvaluationList.as_view(), name='list'),
    url(r'^px_evaluations/(?P<pk>\d+)$', PXEvaluationDetail.as_view(), name='detail'),
    url(r'^px_evaluations/new', PXEvaluationCreation.as_view(), name='new'),
    url(r'^px_evaluations/update/(?P<pk>\d+)', PXEvaluationUpdate.as_view(), name='update'),
    url(r'^px_evaluations/continue/(?P<pk>\d+)', PXEvaluationContinueCreation.as_view(), name='continue'),
]