from django.conf.urls import patterns, include, url
from hello_world import views

urlpatterns = patterns('', 	
	url(r'^hello_world/$', views.hello_view, name='hello_view'),
	url(r'^$', views.hello_view, name='hello_view'),
)
