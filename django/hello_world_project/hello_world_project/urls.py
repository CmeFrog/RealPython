# can use method active here
# or can remove existing url line in urlpatterns
# and uncomment jtn1 or jtn2

from django.conf.urls import patterns, include, url
#jtn2 from hello_world.views import hello_view
from hello_world import views
from hello_world.views import about_view
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_world_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    
    #jtn1 url(r'^hello_world/$', 'hello_world.views.hello_view'),
    #jtn2 url(r'^hello_world/$', hello_view),

    # uses view linked in app dir urls.py
    # routes both hello_world and hello_world/about
    # Note that the regular expression below does not
    # have a $ (end-of-string match character) but does include
    # a trailing slash. Whenever Django encounters include(),
    # it chops off whatever part of the URL matched up to that
    # point and sends the remaining string to the included
    # URLconf for further processing
    url(r'^hello_world/?', include('hello_world.urls')),

    # uses view from imported views file
    url(r'^better/$', views.better_hello),
    
    url(r'^$', include('hello_world.urls')),
)
