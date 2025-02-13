"""RehabExergamesPXApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^', include('apps.dashboard.urls', namespace='dashboard')),
    url(r'^interaction_device/', include('apps.interaction_devices.urls', namespace='interaction_device')),
    url(r'^movements/', include('apps.movements.urls', namespace='movements')),
    url(r'^pathologies/', include('apps.pathologies.urls', namespace='pathologies')),
    url(r'^rehab_exergames/', include('apps.rehab_exergames.urls', namespace='rehab_exergames')),
    url(r'^resources/', include('apps.resources.urls', namespace='resources')),
    url(r'^px_evaluation/', include('apps.px_evaluation.urls', namespace='px_evaluation')),
    url(r'^questionnaire/', include('apps.questionnaires_standard.urls', namespace='questionnaire')),
    url(r'^wiki/', include('apps.wiki.urls', namespace='wiki')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)