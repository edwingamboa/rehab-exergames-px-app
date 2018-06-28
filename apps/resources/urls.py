from django.conf.urls import url

from .views import (
    ResourceCreation,
    ResourceCreationPopUp,
    ResourceDetail,
    ResourceList,
    ResourceUpdate,
)

urlpatterns = [
    url(r'^$', ResourceList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ResourceDetail.as_view(), name='detail'),
    url(r'^new', ResourceCreation.as_view(), name='new'),
    url(r'^pop_up_new', ResourceCreationPopUp.as_view(), name='pop_up_new'),
    url(r'^update/(?P<pk>\d+)$', ResourceUpdate.as_view(), name='update'),
]