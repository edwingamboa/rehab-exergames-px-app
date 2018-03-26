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
    ConstraintCategoryList,
    ConstraintCategoryDetail,
    ConstraintCategoryCreation,
    ConstraintCategoryUpdate,
    ConstraintList,
    ConstraintDetail,
    ConstraintCreation,
    ConstraintUpdate,
)

urlpatterns = [
    url(r'^$', RehabilitationExergameList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', RehabilitationExergameDetail.as_view(), name='detail'),
    url(r'^new', RehabilitationExergameCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', RehabilitationExergameUpdate.as_view(), name='update'),
    url(r'^rehab_task/$', RehabilitationTaskList.as_view(), name='list_task'),
    url(r'^rehab_task/(?P<pk>\d+)$', RehabilitationTaskDetail.as_view(), name='detail_task'),
    url(r'^rehab_task/new', RehabilitationTaskCreation.as_view(), name='new_task'),
    url(r'^rehab_task/update/(?P<pk>\d+)$', RehabilitationTaskUpdate.as_view(), name='update_task'),
    url(r'^constraint_category/$', ConstraintCategoryList.as_view(), name='list_constraint_cat'),
    url(r'^constraint_category/(?P<pk>\d+)$', ConstraintCategoryDetail.as_view(), name='detail_constraint_cat'),
    url(r'^constraint_category/new', ConstraintCategoryCreation.as_view(), name='new_constraint_cat'),
    url(r'^constraint_category/update/(?P<pk>\d+)$', ConstraintCategoryUpdate.as_view(), name='update_constraint_cat'),
    url(r'^constraint/$', ConstraintList.as_view(), name='list_constraint'),
    url(r'^constraint/(?P<pk>\d+)$', ConstraintDetail.as_view(), name='detail_constraint'),
    url(r'^constraint/new', ConstraintCreation.as_view(), name='new_constraint'),
    url(r'^constraint/update/(?P<pk>\d+)$', ConstraintUpdate.as_view(), name='update_constraint'),
]