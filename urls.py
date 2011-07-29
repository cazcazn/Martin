from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import forum.urls
from slideshow.views import ajax_slideshow

admin.autodiscover()

urlpatterns = patterns('',
    (r'^ajax/slideshow/$', ajax_slideshow),
    url(r'^admin/', include(admin.site.urls)),
    (r'^user/', include('registration.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^photologue/', include('photologue.urls')),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns
