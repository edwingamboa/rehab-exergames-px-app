from django.conf.urls import url

from .views import (
    AspectCreation,
    AspectDetail,
    AspectList,
    AspectUpdate,
    MethodCreation,
    MethodDetail,
    MethodList,
    MethodUpdate,
    MethodTypeCreation,
    MethodTypeDetail,
    MethodTypeList,
    MethodTypeUpdate,
    InstrumentCreation,
    InstrumentDetail,
    InstrumentList,
    InstrumentUpdate,
)

urlpatterns = [
    url(r'^aspects/$', AspectList.as_view(), name='list_aspects'),
    url(r'^aspects/(?P<pk>\d+)$', AspectDetail.as_view(), name='detail_aspects'),
    url(r'^aspects/new', AspectCreation.as_view(), name='new_aspects'),
    url(r'^aspects/update/(?P<pk>\d+)$', AspectUpdate.as_view(), name='update_aspects'),
    url(r'^methods/$', MethodList.as_view(), name='list_methods'),
    url(r'^methods/(?P<pk>\d+)$', MethodDetail.as_view(), name='detail_methods'),
    url(r'^methods/new', MethodCreation.as_view(), name='new_methods'),
    url(r'^methods/update/(?P<pk>\d+)$', MethodUpdate.as_view(), name='update_methods'),
    url(r'^method_types/$', MethodTypeList.as_view(), name='list_method_types'),
    url(r'^method_types/(?P<pk>\d+)$', MethodTypeDetail.as_view(), name='detail_method_types'),
    url(r'^method_types/new', MethodTypeCreation.as_view(), name='new_method_types'),
    url(r'^method_types/update/(?P<pk>\d+)$', MethodTypeUpdate.as_view(), name='update_method_types'),
    url(r'^instruments/$', InstrumentList.as_view(), name='list_instruments'),
    url(r'^instruments/(?P<pk>\d+)$', InstrumentDetail.as_view(), name='detail_instruments'),
    url(r'^instruments/new', InstrumentCreation.as_view(), name='new_instruments'),
    url(r'^instruments/update/(?P<pk>\d+)$', InstrumentUpdate.as_view(), name='update_instruments'),
]