from django.conf.urls import url

from .views import (
    ResourceCreation,
    ResourceDetail,
    ResourceList,
    ResourceUpdate,
)

urlpatterns = [
    url(r'^$', ResourceList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ResourceDetail.as_view(), name='detail'),
    url(r'^new', ResourceCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', ResourceUpdate.as_view(), name='update'),
]