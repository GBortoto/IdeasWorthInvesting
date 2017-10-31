from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from iwi_real import views

urlpatterns = [
	url(r'^threads$', views.ThreadList.as_view()),
    url(r'^threads/(?P<pk>[0-9]+)$', views.ThreadDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
