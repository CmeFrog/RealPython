from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('', 
	url(r'^add_post/$', views.add_post, name='add_post'),
#jtn1	url(r'(?P<post_id>\d+)/$', views.post_id, name='post_id'),
#jtn2	url(r'(?P<post_name>\w+)/$', views.post_url, name='post_url'),
	url(r'(?P<post_name>\w+)/$', views.post_url_styles, name='post_url_styles'),
	url(r'^jtn/$', views.jtn, name='jtn'),
#jtn2	url(r'^index_jtn/$', views.index_url, name='index_url'),
	url(r'^index_jtn/$', views.index_url_styles, name='index_url_styles'),
#jtn1	url(r'^$', views.index_id, name='index_id'),
#jtn2	url(r'^$', views.index_url, name='index_url'),
	url(r'^$', views.index_url_styles, name='index_url_styles'),
)