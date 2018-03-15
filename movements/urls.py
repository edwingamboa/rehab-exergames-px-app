from django.conf.urls import url

from .views import (
    MovementList,
    MovementDetail,
    MovementCreation,
    MovementUpdate,
    ConfigurationParameterList,
    ConfigurationParameterDetail,
    ConfigurationParameterCreation,
    ConfigurationParameterUpdate,
)

urlpatterns = [
    url(r'^$', MovementList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', MovementDetail.as_view(), name='detail'),
    url(r'^new', MovementCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', MovementUpdate.as_view(), name='update'),
    url(r'^config_par/$', ConfigurationParameterList.as_view(), name='list_config_par'),
    url(r'^config_par/(?P<pk>\d+)$', ConfigurationParameterDetail.as_view(), name='detail_config_par'),
    url(r'^config_par/new', ConfigurationParameterCreation.as_view(), name='new_config_par'),
    url(r'^config_par/update/(?P<pk>\d+)$', ConfigurationParameterUpdate.as_view(), name='update_config_par'),
]