from django.conf.urls import url

from .views import (
    InteractionDeviceList,
    InteractionDeviceDetail,
    InteractionDeviceCreation,
    InteractionDeviceUpdate,
)

urlpatterns = [
    url(r'^$', InteractionDeviceList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', InteractionDeviceDetail.as_view(), name='detail'),
    url(r'^new', InteractionDeviceCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', InteractionDeviceUpdate.as_view(), name='update'),
]