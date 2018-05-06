from django.conf.urls import url

from .views import (
    AspectCreation,
    AspectDetail,
    AspectList,
    AspectUpdate,
)

urlpatterns = [
    url(r'^aspects/$', AspectList.as_view(), name='list_aspects'),
    url(r'^aspects/(?P<pk>\d+)$', AspectDetail.as_view(), name='detail_aspects'),
    url(r'^aspects/new', AspectCreation.as_view(), name='new_aspects'),
    url(r'^aspects/update/(?P<pk>\d+)$', AspectUpdate.as_view(), name='update_aspects'),
]