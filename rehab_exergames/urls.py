from django.conf.urls import url

from .views import (
    RehabilitationTaskList,
    RehabilitationTaskDetail,
    RehabilitationTaskCreation,
    RehabilitationTaskUpdate,
)

urlpatterns = [
    url(r'^$', RehabilitationTaskList.as_view(), name='list_task'),
    url(r'^(?P<pk>\d+)$', RehabilitationTaskDetail.as_view(), name='detail_task'),
    url(r'^new', RehabilitationTaskCreation.as_view(), name='new_task'),
    url(r'^update/(?P<pk>\d+)$', RehabilitationTaskUpdate.as_view(), name='update_task'),
]