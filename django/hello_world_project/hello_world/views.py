from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime

def hello_view(request):
	return HttpResponse('<html><body>Hello, World!</body></html>')

def about_view(request):
	return HttpResponse("This is the About page. Do you want to return home?<a href='/'> Back Home</a>")
#	return HttpResponse('<html><body>This is the About page. Do you want to return home?<a href="/"> Back Home</a></body></html>')

def better_hello(request):
	t = loader.get_template('betterhello.html')
	c = Context({'current_time' : datetime.now(),})
	return HttpResponse(t.render(c))