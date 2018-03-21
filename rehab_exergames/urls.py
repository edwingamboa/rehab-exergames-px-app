from django.conf.urls import url

from .views import (
    RehabilitationExergameList,
    RehabilitationExergameDetail,
    RehabilitationExergameCreation,
    RehabilitationExergameUpdate,
    RehabilitationTaskList,
    RehabilitationTaskDetail,
    RehabilitationTaskCreation,
    RehabilitationTaskUpdate,
)

urlpatterns = [
    url(r'^$', RehabilitationExergameList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', RehabilitationExergameDetail.as_view(), name='detail'),
    url(r'^new', RehabilitationExergameCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', RehabilitationExergameUpdate.as_view(), name='update'),
    url(r'^rehab_exergame/$', RehabilitationTaskList.as_view(), name='list_task'),
    url(r'^rehab_exergame/(?P<pk>\d+)$', RehabilitationTaskDetail.as_view(), name='detail_task'),
    url(r'^rehab_exergame/new', RehabilitationTaskCreation.as_view(), name='new_task'),
    url(r'^rehab_exergame/update/(?P<pk>\d+)$', RehabilitationTaskUpdate.as_view(), name='update_task'),
]