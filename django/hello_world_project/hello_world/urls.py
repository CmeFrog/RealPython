from django.conf.urls import patterns, include, url
from hello_world import views

urlpatterns = patterns('',
    # handles hello_world/about or hello_world/about/	
	url(r'^about/?', views.about_view, name='about_view'),
	
	url(r'^$', views.hello_view, name='hello_view'),
)
