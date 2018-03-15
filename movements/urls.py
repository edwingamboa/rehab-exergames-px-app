from django.conf.urls import url

from .views import (
    ConfigurationParameterList,
    ConfigurationParameterDetail,
    ConfigurationParameterCreation,
    ConfigurationParameterUpdate,
)

urlpatterns = [
    url(r'^config_par/$', ConfigurationParameterList.as_view(), name='list_config_par'),
    url(r'^config_par/(?P<pk>\d+)$', ConfigurationParameterDetail.as_view(), name='detail_config_par'),
    url(r'^config_par/new', ConfigurationParameterCreation.as_view(), name='new_config_par'),
    url(r'^config_par/update/(?P<pk>\d+)$', ConfigurationParameterUpdate.as_view(), name='update_config_par'),
]