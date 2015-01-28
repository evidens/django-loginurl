from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.conf import settings

from loginurl.views import cleanup, login

urlpatterns = patterns('',
    url(r'^cleanup/$', cleanup, name='loginurl-cleanup'),
    url(r'^(?P<key>[0-9A-Za-z]+-[a-z0-9-]+)/$', login, name='loginurl-login'),
    url(r'^$', RedirectView.as_view(url=settings.LOGIN_URL), name='loginurl-index'),
)
