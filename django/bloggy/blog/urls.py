from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('', 
#	url(r'(?P<post_id>\d+)/$', views.post_id, name='post_id'),
	url(r'(?P<post_name>\w+)/$', views.post_url, name='post_url'),
	url(r'^jtn/$', views.jtn, name='jtn'),
	url(r'^index_jtn/$', views.index_url, name='index_url'),
#	url(r'^$', views.index_id, name='index_id'),
	url(r'^$', views.index_url, name='index_url'),
)