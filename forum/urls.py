from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
  (r'^$', 'forum.views.index'),
  (r'^(?P<forum_id>\d+)/$', 'forum.views.forum_detail'),
  (r'^(?P<forum_id>\d+)/topic/(?P<topic_id>\d+)/$', 'forum.views.topic_detail'),
)
