from django.conf.urls import url

from .views import (
    DefinitionCreation,
    DefinitionDetail,
    DefinitionList,
    DefinitionUpdate,
    DefinitionCreationPopUp,
)

urlpatterns = [
    url(r'^definitions/$', DefinitionList.as_view(), name='list_definitions'),
    url(r'^definitions/(?P<pk>\d+)$', DefinitionDetail.as_view(), name='detail_definitions'),
    url(r'^definitions/new', DefinitionCreation.as_view(), name='new_definitions'),
    url(r'^definitions/update/(?P<pk>\d+)$', DefinitionUpdate.as_view(), name='update_definitions'),
    url(r'^definitions/pop_up_new', DefinitionCreationPopUp.as_view(), name='pop_up_new_definitions'),
]