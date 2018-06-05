from django.conf.urls import url

from .views import (
    InteractionDeviceList,
    InteractionDeviceDetail,
    InteractionDeviceCreation,
    InteractionDeviceUpdate,
    DeviceTechnologyList,
    DeviceTechnologyDetail,
    DeviceTechnologyCreation,
    DeviceTechnologyCreationPopUp,
    DeviceTechnologyUpdate,
)

urlpatterns = [
    url(r'^$', InteractionDeviceList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', InteractionDeviceDetail.as_view(), name='detail'),
    url(r'^new', InteractionDeviceCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', InteractionDeviceUpdate.as_view(), name='update'),
    url(r'^device_tech/$', DeviceTechnologyList.as_view(), name='list_tech'),
    url(r'^device_tech/(?P<pk>\d+)$', DeviceTechnologyDetail.as_view(), name='detail_tech'),
    url(r'^device_tech/new', DeviceTechnologyCreation.as_view(), name='new_tech'),
    url(r'^device_tech/pop_up_new', DeviceTechnologyCreationPopUp.as_view(), name='pop_up_new_tech'),
    url(r'^device_tech/update/(?P<pk>\d+)$', DeviceTechnologyUpdate.as_view(), name='update_tech'),
]