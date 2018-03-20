from django.conf.urls import url

from .views import (
    PathologyList,
    PathologyDetail,
    PathologyCreation,
    PathologyUpdate,
)

urlpatterns = [
    url(r'^$', PathologyList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PathologyDetail.as_view(), name='detail'),
    url(r'^new', PathologyCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', PathologyUpdate.as_view(), name='update'),
]